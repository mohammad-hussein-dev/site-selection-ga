"""
Visualization utilities for site selection results.

This module provides functions to plot candidate points, selected schools,
and existing facilities (libraries, hospitals, fire stations).
"""

from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np


def plot_results(
    points: np.ndarray,
    selected_indices: List[int],
    libraries: np.ndarray,
    hospitals: np.ndarray,
    fire_stations: np.ndarray,
    save_path: Optional[str] = None,
    show: bool = True,
) -> None:
    """
    Plot the candidate points, selected schools, and existing facilities.

    This function creates a 2D scatter plot where:
        - Blue dots represent all candidate points.
        - Red stars highlight the selected school locations.
        - Green triangles, orange squares, and purple diamonds mark
          libraries, hospitals, and fire stations respectively.

    Args:
        points: Array of shape (n_points, 2) with candidate coordinates.
        selected_indices: List of indices for the selected schools.
        libraries: Array of shape (n_libs, 2) with library coordinates.
        hospitals: Array of shape (n_hosp, 2) with hospital coordinates.
        fire_stations: Array of shape (n_fire, 2) with fire station coordinates.
        save_path: Optional file path to save the figure (e.g., "plot.png").
        show: If True, display the plot; otherwise, close it after saving.
    """
    plt.figure(figsize=(14, 10), facecolor='white')

    # ---- Candidate points ----
    plt.scatter(
        points[:, 0], points[:, 1],
        c='blue', alpha=0.4, s=40,
        label='Candidate Points'
    )

    # ---- Selected schools (highlighted with stars) ----
    selected_points = points[selected_indices]
    plt.scatter(
        selected_points[:, 0], selected_points[:, 1],
        c='red', s=350, marker='*',
        edgecolors='black', linewidth=2,
        label='Selected Schools'
    )

    # ---- Facilities ----
    plt.scatter(
        libraries[:, 0], libraries[:, 1],
        c='green', marker='^', s=180,
        label='Libraries'
    )
    plt.scatter(
        hospitals[:, 0], hospitals[:, 1],
        c='orange', marker='s', s=180,
        label='Hospitals'
    )
    plt.scatter(
        fire_stations[:, 0], fire_stations[:, 1],
        c='purple', marker='D', s=180,
        label='Fire Stations'
    )

    # ---- Annotate selected points with labels ----
    for i, idx in enumerate(selected_indices):
        plt.annotate(
            f'School #{i+1}',
            (points[idx, 0] + 2, points[idx, 1] + 2),
            fontsize=13, fontweight='bold', color='darkred',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8)
        )

    # ---- Styling ----
    plt.title(
        'Optimal School Site Selection using Genetic Algorithm',
        fontsize=18, fontweight='bold', pad=20
    )
    plt.xlabel('X Coordinate', fontsize=13)
    plt.ylabel('Y Coordinate', fontsize=13)
    plt.legend(loc='upper right', fontsize=12, framealpha=0.9)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()

    # ---- Save or show ----
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Plot saved as '{save_path}'")

    if show:
        plt.show()
    else:
        plt.close()
