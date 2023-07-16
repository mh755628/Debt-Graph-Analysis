import time
from genetic import *



for n in range(2, 100):
    debt = [0] * n

    start = time.time()

    GENERATIONS = 10000

    population = getInitialPopulation(n, debt)

    for _ in range(GENERATIONS):
        population = getNextGen(population, debt)
    
    end = time.time()