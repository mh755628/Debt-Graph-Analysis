from viz_graph import create_graph
from random import shuffle, randint

POPULATION_SIZE = 50
MUTATION_RATE   = 7

def fitness(permutation, debt):
    nw_debt = [debt[i] for i in permutation]
    in_debt, in_cred, edges = create_graph(nw_debt)
    return len(edges)

#check if permutation is valid

def isValid(permutation):
    n  = len(permutation)
    s = [0] * n
    for x in permutation:
        if x >= n or x < 0 or s[x]:
            return False
        s[x] = 1
    return True

class Gene:
    def __init__(self, permutation, debt):
        self.permutation = permutation
        self.reverse_map = [0] * len(permutation)
        self.fitness = fitness(permutation, debt)

        for i in range(len(permutation)):
            self.reverse_map[permutation[i]] = i
    
    
    
    def mutate(self, debt):
        #swap, reverse

        def swap():
            i, j = sorted([randint(0, len(self.permutation) - 1) for _ in range(2)])
            self.permutation[i], self.permutation[j] = self.permutation[j], self.permutation[i]

            if not isValid(self.permutation):
                print("Invalid swap")

                #throw exception

                Exception("Invalid swap")

            self.fitness = fitness(self.permutation, debt)

        def reverse():
            i, j = sorted([randint(0, len(self.permutation) - 1) for _ in range(2)])
            self.permutation[i:j] = reversed(self.permutation[i:j])

            if not isValid(self.permutation):
                print("Invalid reverse")
                #throw exception

                Exception("Invalid reverse")
            
            self.fitness = fitness(self.permutation, debt)

        #3% chance to mutate
        if randint(0, 100) < MUTATION_RATE:
            #50% chance to swap
            if randint(0, 1):
                swap()
            else:
                reverse()


    def cycle_crossover(self, other, debt):
        n = len(self.permutation)

        p1 = [x for x in self.permutation]
        p2 = [x for x in other.permutation]

        g1 = Gene(p1, debt)
        g2 = Gene(p2, debt)

        visit = [False] * n

        child1 = [0] * n
        child2 = [0] * n

        cycle_parity = 0

        for i in range(n):
            if visit[i]:
                continue

            j = i

            cycle_parity ^= 1

            if cycle_parity:
                g1, g2 = g2, g1

            while not visit[j]:
                visit[j] = True
                child1[j] = g1.permutation[j]
                child2[j] = g2.permutation[j]

                j = g1.reverse_map[g2.permutation[j]]


        if (not isValid(child1)) or (not isValid(child2)):
            print("Invalid crossover") 

            print(self.permutation)
            print(other.permutation)

            print(child1)
            print(child2)

            #raise Exception("Invalid crossover")

            Exception("Invalid crossover")

        return Gene(child1, debt), Gene(child2, debt)
                

def getRandomGene(n, debt):
    permutation = list(range(n))
    shuffle(permutation)
    return Gene(permutation, debt)

def getInitialPopulation(n, debt):
    return [getRandomGene(n, debt) for _ in range(POPULATION_SIZE)]


def getNextGen(population, debt):
    #selection
    # population.sort(key=lambda gene: gene.fitness(debt))
    # print(population[0].fitness(debt))
    #sort by fitness

    population.sort(key=lambda gene: gene.fitness)

    population = population[:POPULATION_SIZE]

    n = len(population)

    #crossover
    for i in range(0, n, 2):
        population.extend(population[i].cycle_crossover(population[i + 1], debt))


    for i in range(n):
        #select random gene to mutate
        j = randint(0, len(population) - 1)
        population.extend(population[i].cycle_crossover(population[j], debt))

    #mutation
    for gene in population:
        gene.mutate(debt)

    return population