"""
Genetic Algorithm implementation for optimal school site selection.

This module provides the main optimization routine using DEAP library
to evolve a population of candidate solutions (sets of 3 locations).
"""

import random
from typing import Any, List, Tuple

import numpy as np
from deap import algorithms, base, creator, tools

from .fitness import fitness_function


def run_ga(
    points: np.ndarray,
    population: np.ndarray,
    libraries: np.ndarray,
    hospitals: np.ndarray,
    fire_stations: np.ndarray,
    n_points: int = 100,
    n_select: int = 3,
    pop_size: int = 50,
    ngen: int = 100,
    cxpb: float = 0.5,
    mutpb: float = 0.2,
    verbose: bool = True,
) -> Tuple[List[int], float, Any]:
    """
    Run the Genetic Algorithm to find optimal school locations.

    This function sets up and executes a genetic algorithm using the DEAP library.
    It evolves a population of solutions (each representing 3 candidate indices)
    toward maximizing the fitness function defined in the `fitness` module.

    Args:
        points: Array of shape (n_points, 2) with candidate coordinates.
        population: Array of shape (n_points,) with population densities.
        libraries: Array of library coordinates.
        hospitals: Array of hospital coordinates.
        fire_stations: Array of fire station coordinates.
        n_points: Total number of candidate points (default: 100).
        n_select: Number of points to select (must be 3 for this problem).
        pop_size: Size of the GA population (default: 50).
        ngen: Number of generations to evolve (default: 100).
        cxpb: Crossover probability (default: 0.5).
        mutpb: Mutation probability (default: 0.2).
        verbose: If True, print progress during evolution (default: True).

    Returns:
        A tuple containing:
            - best_indices: List of 3 indices of the best solution.
            - best_fitness: The fitness value of the best solution.
            - log: The evolution statistics log from DEAP.

    Raises:
        ValueError: If n_select is not 3 (the problem requires exactly 3 schools).
    """
    if n_select != 3:
        raise ValueError("This implementation is designed for selecting exactly 3 locations.")

    # ---- DEAP setup ----
    # Create fitness and individual types
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    # Generate a random solution: sample n_select unique indices from 0..n_points-1
    toolbox.register("indices", random.sample, range(n_points), n_select)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Evaluation function: returns fitness as a tuple
    def eval_fitness(individual: List[int]) -> Tuple[float]:
        return fitness_function(individual, points, population, libraries, hospitals, fire_stations)

    toolbox.register("evaluate", eval_fitness)

    # Genetic operators
    toolbox.register("mate", tools.cxTwoPoint)           # Two-point crossover
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)  # Shuffle mutation
    toolbox.register("select", tools.selTournament, tournsize=3)     # Tournament selection

    # ---- Initialization ----
    pop = toolbox.population(n=pop_size)
    hof = tools.HallOfFame(1)  # Hall of Fame to store the best individual
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)

    # ---- Evolution ----
    pop, log = algorithms.eaSimple(
        pop,
        toolbox,
        cxpb=cxpb,
        mutpb=mutpb,
        ngen=ngen,
        stats=stats,
        halloffame=hof,
        verbose=verbose,
    )

    # ---- Extract best solution ----
    best_indices = hof[0]
    best_fitness = hof[0].fitness.values[0]

    return best_indices, best_fitness, log
