#!/usr/bin/env python
"""
Main entry point for the site selection optimization.

This script generates synthetic data, runs the Genetic Algorithm,
and displays the results with a plot.
"""

from typing import Tuple

import numpy as np

from src.site_selection import plot_results, run_ga


def generate_data(seed: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate synthetic data for demonstration purposes.

    This function creates random candidate points, population densities,
    and facility locations to illustrate the optimization process.

    Args:
        seed: Random seed for reproducibility (default: 42).

    Returns:
        A tuple containing:
            - points: Array of shape (100, 2) with candidate coordinates.
            - population: Array of shape (100,) with population densities.
            - libraries: Array of shape (5, 2) with library coordinates.
            - hospitals: Array of shape (3, 2) with hospital coordinates.
            - fire_stations: Array of shape (3, 2) with fire station coordinates.
    """
    np.random.seed(seed)
    n_points = 100
    points = np.random.rand(n_points, 2) * 100
    population = np.random.randint(50, 500, n_points)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100
    return points, population, libraries, hospitals, fire_stations


def main() -> None:
    """
    Run the optimization and display results.

    This is the main execution function that:
        1. Generates synthetic data.
        2. Runs the Genetic Algorithm.
        3. Prints the optimal solution.
        4. Plots the results.
    """
    # Generate synthetic data
    points, population, libraries, hospitals, fire_stations = generate_data()

    # Run the Genetic Algorithm
    best_indices, best_fitness, _ = run_ga(
        points=points,
        population=population,
        libraries=libraries,
        hospitals=hospitals,
        fire_stations=fire_stations,
        n_points=100,
        n_select=3,
        pop_size=50,
        ngen=100,
        verbose=True,
    )

    # Print the final results
    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    print(f"Selected indices: {best_indices}")
    print(f"Coordinates: {points[best_indices]}")
    print(f"Fitness value: {best_fitness:.4f}")
    print("=" * 60)

    # Plot the results
    plot_results(
        points=points,
        selected_indices=best_indices,
        libraries=libraries,
        hospitals=hospitals,
        fire_stations=fire_stations,
        save_path="site_selection_result.png",
        show=True,
    )


if __name__ == "__main__":
    main()
