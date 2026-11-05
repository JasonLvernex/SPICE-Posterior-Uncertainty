"""Display-only orientation helpers for 2-D spatial maps."""

from __future__ import annotations

import numpy as np


def orient_map_for_display(array: np.ndarray) -> np.ndarray:
    """Rotate a spatial map 90 degrees counter-clockwise for figure display."""
    arr = np.asarray(array)
    if arr.ndim < 2:
        raise ValueError(f"Expected at least 2 dimensions, got shape {arr.shape}")
    return np.rot90(arr, k=1, axes=(0, 1))


def orient_point_for_display(
    voxel_x: float,
    voxel_y: float,
    spatial_shape: tuple[int, int],
) -> tuple[float, float]:
    """Map an original (column, row) coordinate onto the rotated display."""
    _, n_cols = spatial_shape
    return voxel_y, n_cols - 1 - voxel_x
