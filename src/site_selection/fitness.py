"""Fitness function for site selection problem."""

import numpy as np


def fitness_function(selected_indices, points, population,
                     libraries, hospitals, fire_stations):
    """
    Calculate fitness for selected school locations.

    Criteria:
    1. Population coverage (maximize)
    2. Distance to facilities (minimize)
    3. Uniform distribution (maximize)

    Returns:
        float: Fitness value (higher is better)
    """
    selected_points = points[selected_indices]

    # Criterion 1: Population coverage
    coverage = np.sum(population[selected_indices])

    # Criterion 2: Distance to facilities
    min_dist_lib = np.min([
        np.min(np.linalg.norm(p - libraries, axis=1))
        for p in selected_points
    ])
    min_dist_hosp = np.min([
        np.min(np.linalg.norm(p - hospitals, axis=1))
        for p in selected_points
    ])
    min_dist_fire = np.min([
        np.min(np.linalg.norm(p - fire_stations, axis=1))
        for p in selected_points
    ])

    # Criterion 3: Spatial spread
    if len(selected_indices) == 3:
        d1 = np.linalg.norm(selected_points[0] - selected_points[1])
        d2 = np.linalg.norm(selected_points[1] - selected_points[2])
        d3 = np.linalg.norm(selected_points[2] - selected_points[0])
        spread = (d1 + d2 + d3) / 3
    else:
        spread = 0

    # Weighted sum (customizable)
    fitness = (
        (coverage / 500) * 0.5 +
        (spread / 50) * 0.3 -
        (min_dist_lib + min_dist_hosp + min_dist_fire) * 0.2
    )

    return (float(fitness),)
