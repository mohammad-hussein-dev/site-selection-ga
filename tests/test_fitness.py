"""Tests for fitness function."""

import numpy as np
import pytest
from src.site_selection.fitness import fitness_function


def test_fitness_function_returns_float():
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
    points = np.random.rand(100, 2) * 100
    population = np.random.randint(50, 500, 100)
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100
    selected = [10, 20, 30]

    result = fitness_function(selected, points, population,
                              libraries, hospitals, fire_stations)
    assert result[0] is not None
