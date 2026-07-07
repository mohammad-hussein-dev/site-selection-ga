"""Tests for visualization module."""

import os
import numpy as np
from src.site_selection.visualization import plot_results


def test_plot_results_runs_without_error():
    points = np.random.rand(100, 2) * 100
    selected = [10, 20, 30]
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    plot_results(points, selected, libraries, hospitals, fire_stations,
                 show=False, save_path=None)


def test_plot_results_saves_file():
    points = np.random.rand(100, 2) * 100
    selected = [10, 20, 30]
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    plot_results(points, selected, libraries, hospitals, fire_stations,
                 show=False, save_path="test_plot.png")

    assert os.path.exists("test_plot.png")
    os.remove("test_plot.png")


def test_plot_results_with_show_true():
    """Test plot_results with show=True to cover plt.show() branch."""
    points = np.random.rand(100, 2) * 100
    selected = [10, 20, 30]
    libraries = np.random.rand(5, 2) * 100
    hospitals = np.random.rand(3, 2) * 100
    fire_stations = np.random.rand(3, 2) * 100

    plot_results(points, selected, libraries, hospitals, fire_stations,
                 show=True, save_path=None)
    assert True
