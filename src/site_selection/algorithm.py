"""Genetic Algorithm implementation for site selection."""

import random

import numpy as np
from deap import algorithms, base, creator, tools

from .fitness import fitness_function


def run_ga(points, population, libraries, hospitals, fire_stations,
           n_points=100, n_select=3, pop_size=50, ngen=100,
           cxpb=0.5, mutpb=0.2, verbose=True):
    """
    Run Genetic Algorithm for optimal site selection.

    Args:
        points: Candidate point coordinates (n_points, 2)
        population: Population density for each point
        libraries: Library locations
        hospitals: Hospital locations
        fire_stations: Fire station locations
        n_points: Total candidate points
        n_select: Number of sites to select
        pop_size: Population size for GA
        ngen: Number of generations
        cxpb: Crossover probability
        mutpb: Mutation probability
        verbose: Print progress

    Returns:
        best_indices: Selected point indices
        best_fitness: Fitness value of best solution
        log: Evolution statistics
    """

    # Create fitness and individual types
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(n_points), n_select)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def eval_fitness(individual):
        return (fitness_function(individual, points, population,
                                 libraries, hospitals, fire_stations)[0],)

    toolbox.register("evaluate", eval_fitness)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=pop_size)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)

    pop, log = algorithms.eaSimple(
        pop, toolbox,
        cxpb=cxpb,
        mutpb=mutpb,
        ngen=ngen,
        stats=stats,
        halloffame=hof,
        verbose=verbose
    )

    best_indices = hof[0]
    best_fitness = hof[0].fitness.values[0]

    return best_indices, best_fitness, log
