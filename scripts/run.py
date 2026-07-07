#!/usr/bin/env python
"""Main script to run the site selection optimization."""

import numpy as np

from src.site_selection import plot_results, run_ga


def generate_data(seed=42):
    """Generate synthetic data for demonstration."""
    np.random.seed(seed)
    n_points = 100
    points = np.random.rand(n_points, 2) * 100
    population = np.random.randint(50, 500, n_points)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100
    return points, population, libraries, hospitals, fire_stations


def main():
    points, population, libraries, hospitals, fire_stations = generate_data()

    best_indices, best_fitness, log = run_ga(
        points=points,
        population=population,
        libraries=libraries,
        hospitals=hospitals,
        fire_stations=fire_stations,
        n_points=100,
        n_select=3,
        pop_size=50,
        ngen=100,
        verbose=True
    )

    print("\n" + "=" * 60)
    print("🏫 FINAL RESULT / نتیجه نهایی")
    print("=" * 60)
    print(f"📌 Selected indices: {best_indices}")
    print(f"📍 Coordinates: {points[best_indices]}")
    print(f"⭐ Fitness value: {best_fitness:.4f}")
    print("=" * 60)

    plot_results(
        points=points,
        selected_indices=best_indices,
        libraries=libraries,
        hospitals=hospitals,
        fire_stations=fire_stations,
        save_path="site_selection_result.png",
        show=True
    )


if __name__ == "__main__":
    main()
