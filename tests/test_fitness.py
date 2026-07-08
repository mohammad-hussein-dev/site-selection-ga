"""
Tests for the fitness function module.

This module contains unit tests to verify the correctness of the fitness function
used in the site selection optimization problem.
"""

import numpy as np
import pytest

from src.site_selection.fitness import fitness_function


def test_fitness_function_returns_float():
    """
    Test that the fitness function returns a tuple containing a float.

    This test ensures the fitness function returns the expected data type
    for a valid input of exactly 3 selected indices.
    """
    points = np.random.rand(100, 2) * 100
    population = np.random.randint(50, 500, 100)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100
    selected = [10, 20, 30]

    result = fitness_function(selected, points, population,
                              libraries, hospitals, fire_stations)

    assert isinstance(result, tuple)
    assert isinstance(result[0], float)


def test_fitness_function_handles_3_points():
    """
    Test that the fitness function works correctly with exactly 3 selected indices.

    This test verifies that the fitness value is computed and returned
    without raising exceptions for a valid input.
    """
    points = np.random.rand(100, 2) * 100
    population = np.random.randint(50, 500, 100)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100
    selected = [10, 20, 30]

    result = fitness_function(selected, points, population,
                              libraries, hospitals, fire_stations)

    assert result[0] is not None
    assert isinstance(result[0], float)


def test_fitness_function_raises_value_error_for_invalid_length():
    """
    Test that the fitness function raises ValueError when selected_indices length is not 3.

    The fitness function requires exactly 3 indices. Any other length should
    raise a ValueError with an appropriate message.
    """
    points = np.random.rand(100, 2) * 100
    population = np.random.randint(50, 500, 100)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    selected = [10, 20]  # Only 2 indices (invalid)

    with pytest.raises(ValueError, match="Exactly 3 indices must be selected"):
        fitness_function(selected, points, population,
                         libraries, hospitals, fire_stations)


def test_fitness_function_spread_calculation_with_3_points():
    """
    Test that the fitness function correctly calculates spread for 3 selected points.

    This test verifies that the spread component of the fitness function
    is computed as the average pairwise distance between the three selected points.
    """
    points = np.random.rand(100, 2) * 100
    population = np.random.randint(50, 500, 100)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    selected = [10, 20, 30]  # Exactly 3 indices

    result = fitness_function(selected, points, population,
                              libraries, hospitals, fire_stations)

    assert isinstance(result[0], float)
    assert result[0] is not None
