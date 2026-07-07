"""Tests for genetic algorithm."""

import numpy as np

from src.site_selection.algorithm import run_ga


def test_run_ga_returns_correct_shape():
    points = np.random.rand(100, 2) * 100
    population = np.random.randint(50, 500, 100)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    best_indices, best_fitness, log = run_ga(
        points=points,
        population=population,
        libraries=libraries,
        hospitals=hospitals,
        fire_stations=fire_stations,
        verbose=False
    )

    assert len(best_indices) == 3
    assert isinstance(best_fitness, float)
    assert hasattr(log, "select")
