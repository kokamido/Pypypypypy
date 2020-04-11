from typing import Tuple, Dict, Callable

import numpy as np
from scipy.integrate import odeint


def integrate1d(func: Callable[[np.ndarray, float], np.ndarray],
                params: Tuple,
                time_points: np.ndarray,
                init_values: np.ndarray) \
        -> Tuple[np.ndarray, Dict[str, any]]:
    data, meta = odeint(func, init_values, time_points, args=params, ml=2, mu=2, full_output=1)
    return data, meta

def integrate0d(func: Callable[[np.ndarray, float], np.ndarray],
                params: Tuple,
                time_points: np.ndarray,
                init_values: np.ndarray) \
        -> Tuple[np.ndarray, Dict[str, any]]:
    data, meta = odeint(func, init_values, time_points, args=params, full_output=1)
    return data, meta

def calc_difference(a: np.ndarray, b: np.ndarray) -> float:
    return np.sum(np.abs(a - b))


def neyavnaya_shema2d(data: np.ndarray, make_matrix: Callable[[np.ndarray], np.ndarray],
                    make_b: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    return np.linalg.solve(make_matrix(data),make_b(data))
