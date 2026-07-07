"""Tests for visualization module."""

import matplotlib
matplotlib.use('Agg')  # Force non-interactive backend for CI
import matplotlib.pyplot as plt
import numpy as np
import os
from src.site_selection.visualization import plot_results


def test_plot_results_runs_without_error():
    """Test that plot_results executes without raising an exception."""
    points = np.random.rand(100, 2) * 100
    selected = [10, 20, 30]
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    # Run with show=False to avoid displaying the plot during tests
    plot_results(points, selected, libraries, hospitals, fire_stations,
                 show=False, save_path=None)

    # Assert that no exception was raised (test passes implicitly)


def test_plot_results_saves_file():
    """Test that plot_results can save a file."""
    points = np.random.rand(100, 2) * 100
    selected = [10, 20, 30]
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    plot_results(points, selected, libraries, hospitals, fire_stations,
                 show=False, save_path="test_plot.png")

    assert os.path.exists("test_plot.png")
    os.remove("test_plot.png")
