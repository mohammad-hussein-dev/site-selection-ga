"""
Fitness function for the site selection optimization problem.

This module defines the multi-criteria fitness function used by the Genetic Algorithm
to evaluate candidate solutions (sets of 3 school locations).
"""

import numpy as np
from typing import List, Tuple


def fitness_function(
    selected_indices: List[int],
    points: np.ndarray,
    population: np.ndarray,
    libraries: np.ndarray,
    hospitals: np.ndarray,
    fire_stations: np.ndarray,
) -> Tuple[float]:
    """
    Calculate the fitness value for a set of selected candidate points.

    The fitness function combines three objectives with custom weights:
        1. Population coverage (maximized) — sum of population in selected areas.
        2. Distance to facilities (minimized) — proximity to libraries, hospitals, fire stations.
        3. Spatial distribution (maximized) — average distance between selected points.

    Args:
        selected_indices: List of exactly 3 indices representing the chosen candidate points.
        points: Array of shape (n_points, 2) containing coordinates of all candidates.
        population: Array of shape (n_points,) with population density for each candidate.
        libraries: Array of shape (n_libs, 2) with library coordinates.
        hospitals: Array of shape (n_hosp, 2) with hospital coordinates.
        fire_stations: Array of shape (n_fire, 2) with fire station coordinates.

    Returns:
        Tuple[float]: A single-element tuple containing the fitness value (higher is better).

    Raises:
        ValueError: If selected_indices does not contain exactly 3 elements.
    """
    if len(selected_indices) != 3:
        raise ValueError("Exactly 3 indices must be selected for fitness evaluation.")

    selected_points = points[selected_indices]

    # ---- Criterion 1: Population coverage ----
    # Sum of population densities of the selected points
    coverage = np.sum(population[selected_indices])

    # ---- Criterion 2: Distance to facilities ----
    # For each selected point, compute the minimum distance to the nearest library,
    # hospital, and fire station. Then take the average across selected points.
    # Smaller distances are better, so this criterion is subtracted.
    min_dist_lib = np.min([
        np.min(np.linalg.norm(p - libraries, axis=1)) for p in selected_points
    ])
    min_dist_hosp = np.min([
        np.min(np.linalg.norm(p - hospitals, axis=1)) for p in selected_points
    ])
    min_dist_fire = np.min([
        np.min(np.linalg.norm(p - fire_stations, axis=1)) for p in selected_points
    ])

    # ---- Criterion 3: Spatial distribution ----
    # Compute the average pairwise distance between the three selected points.
    # Larger spread means better coverage of the city area.
    d1 = np.linalg.norm(selected_points[0] - selected_points[1])
    d2 = np.linalg.norm(selected_points[1] - selected_points[2])
    d3 = np.linalg.norm(selected_points[2] - selected_points[0])
    spread = (d1 + d2 + d3) / 3.0

    # ---- Combine criteria with custom weights ----
    # Weights are chosen to prioritize population coverage (50%),
    # while also considering spread (30%) and proximity to facilities (20%).
    # Normalization factors (500, 50) are used to scale each term to a similar range.
    fitness = (
        (coverage / 500.0) * 0.5
        + (spread / 50.0) * 0.3
        - (min_dist_lib + min_dist_hosp + min_dist_fire) * 0.2
    )

    return (float(fitness),)
