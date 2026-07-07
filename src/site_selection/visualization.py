"""Visualization utilities for site selection results."""

import matplotlib.pyplot as plt
import numpy as np


def plot_results(points, selected_indices, libraries, hospitals, fire_stations,
                 save_path=None, show=True):
    """
    Plot candidate points, selected sites, and facilities.

    Args:
        points: All candidate points
        selected_indices: Indices of selected points
        libraries: Library locations
        hospitals: Hospital locations
        fire_stations: Fire station locations
        save_path: Path to save the figure (optional)
        show: Whether to display the figure
    """
    plt.figure(figsize=(14, 10), facecolor='white')

    # Candidate points
    plt.scatter(points[:, 0], points[:, 1],
                c='blue', alpha=0.4, s=40,
                label='Candidate Points / نقاط کاندید')

    # Selected schools
    selected_points = points[selected_indices]
    plt.scatter(selected_points[:, 0], selected_points[:, 1],
                c='red', s=350, marker='*',
                edgecolors='black', linewidth=2,
                label='Selected Schools / مدارس انتخاب‌شده')

    # Facilities
    plt.scatter(libraries[:, 0], libraries[:, 1],
                c='green', marker='^', s=180,
                label='Libraries / کتابخانه‌ها')
    plt.scatter(hospitals[:, 0], hospitals[:, 1],
                c='orange', marker='s', s=180,
                label='Hospitals / بیمارستان‌ها')
    plt.scatter(fire_stations[:, 0], fire_stations[:, 1],
                c='purple', marker='D', s=180,
                label='Fire Stations / آتش‌نشانی‌ها')

    # Annotate selected points
    for i, idx in enumerate(selected_indices):
        plt.annotate(f'School #{i+1}',
                     (points[idx, 0] + 2, points[idx, 1] + 2),
                     fontsize=13, fontweight='bold', color='darkred',
                     bbox=dict(boxstyle='round,pad=0.3',
                               facecolor='white', alpha=0.8))

    plt.title('Optimal School Site Selection using Genetic Algorithm\n'
              'مکان‌یابی بهینه مدارس با الگوریتم ژنتیک',
              fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('X Coordinate / مختصات X', fontsize=13)
    plt.ylabel('Y Coordinate / مختصات Y', fontsize=13)
    plt.legend(loc='upper right', fontsize=12, framealpha=0.9)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Plot saved as '{save_path}'")

    if show:
        plt.show()
    else:
        plt.close()
