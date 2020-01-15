import numpy as np
from scipy.integrate import odeint
from typing import Tuple, Dict, Callable


def integrate1d(func: Callable[[np.ndarray, float], np.ndarray],
                params: Tuple,
                time_points: np.ndarray,
                init_values: np.ndarray) \
        -> Tuple[np.ndarray, Dict[str, any]]:
    data, meta = odeint(func, init_values, time_points, args=params, ml=2, mu=2, full_output=True)
    return data, meta


def calc_difference(a: np.ndarray, b: np.ndarray) -> float:
    return np.sum(np.abs(a - b))
