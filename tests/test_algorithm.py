"""
Tests for the Genetic Algorithm module.

This module contains unit tests to verify the correctness of the GA implementation
for the site selection optimization problem.
"""

import numpy as np
import pytest

from src.site_selection.algorithm import run_ga


def test_run_ga_returns_correct_shape():
    """
    Test that run_ga returns the expected data types and shapes.

    This test ensures the GA returns a list of 3 indices, a float fitness value,
    and a log object, confirming the algorithm runs correctly with valid inputs.
    """
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
        verbose=False,
    )

    assert len(best_indices) == 3
    assert isinstance(best_fitness, float)
    assert hasattr(log, "select")


def test_run_ga_raises_value_error_for_invalid_n_select():
    """
    Test that run_ga raises ValueError when n_select is not 3.

    The algorithm is designed specifically for selecting exactly 3 locations.
    Any other value should raise a ValueError with an appropriate message.
    """
    points = np.random.rand(100, 2) * 100
    population = np.random.randint(50, 500, 100)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    with pytest.raises(ValueError, match="This implementation is designed for selecting exactly 3 locations."):
        run_ga(
            points=points,
            population=population,
            libraries=libraries,
            hospitals=hospitals,
            fire_stations=fire_stations,
            n_select=2,  # Invalid: should be 3
            verbose=False,
        )
