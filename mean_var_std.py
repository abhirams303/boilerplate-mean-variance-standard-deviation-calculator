import numpy as np


def calculate(values):

    if len(values) != 9:
        raise ValueError("List must contain nine numbers.")

    grid = np.array(values).reshape(3, 3)

    as_list = lambda arr: arr.tolist()

    stat_map = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum
    }

    results = {}
    for name, func in stat_map.items():
        axis0 = as_list(func(grid, axis=0))
        axis1 = as_list(func(grid, axis=1))
        flat  = func(grid)  # scalar
        results[name] = [axis0, axis1, flat if np.isscalar(flat) else as_list(flat)]

    return results
