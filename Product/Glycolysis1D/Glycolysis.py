from typing import Dict, Any

import numpy as np

from Product import MathHelper as mh
from Product.SystemSettings import SystemSettings


class GlycolysisSettings(SystemSettings):
    p: float = None
    q: float = None
    Du: float = None
    Dv: float = None
    dx: float = None

    def __init__(self, p: float, q: float, Du: float, Dv: float, dx: float):
        self.p = p
        self.q = q
        self.Du = Du
        self.Dv = Dv
        self.dx = dx
        self.steps = {'dx': dx}
        self.params = {'p': p, 'q': q, 'Du': Du, 'Dv': Dv}

    def as_tuple(self):
        return self.p, self.q, self.Du, self.Dv, self.dx

    def to_dict(self) -> Dict[str, Any]:
        return {
            'p': self.p,
            'q': self.q,
            'Du': self.Du,
            'Dv': self.Dv,
            'dx': self.dx
        }

    def __to_str(self) -> str:
        return str(self.to_dict())

    def __str__(self):
        return self.__to_str()

    def __repr__(self):
        return self.__to_str()


def run(glycolysis_settings: GlycolysisSettings, time_points: np.ndarray, init_condition: np.ndarray):
    return mh.integrate1d(__glycolysis, glycolysis_settings.as_tuple(), time_points, init_condition)


def calc_Du_crit(p: float, q: float, Dv: float) -> float:
    return (q + 1) / p * (2 * q + 1 + 2 * np.sqrt(q * (q + 1))) * Dv


def __f(u: np.ndarray, v: np.ndarray, p: float, q: float) -> np.ndarray:
    return 1 - u * v


def __g(u: np.ndarray, v: np.ndarray, p: float, q: float) -> np.ndarray:
    return p * v * (u - (1 + q) / (q + v))


def __glycolysis(y: np.ndarray, t: float, p: float, q: float, Du: float, Dv: float, dx: float) -> np.ndarray:
    u = y[::2]
    v = y[1::2]
    dydt = np.empty_like(y)
    dudt = dydt[::2]
    dvdt = dydt[1::2]

    dudt[0] = __f(u[0], v[0], p, q) + Du * (-2.0 * u[0] + 2.0 * u[1]) / dx ** 2
    dudt[1:-1] = __f(u[1:-1], v[1:-1], p, q) + Du * np.diff(u, 2) / dx ** 2
    dudt[-1] = __f(u[-1], v[-1], p, q) + Du * (- 2.0 * u[-1] + 2.0 * u[-2]) / dx ** 2
    dvdt[0] = __g(u[0], v[0], p, q) + Dv * (-2.0 * v[0] + 2.0 * v[1]) / dx ** 2
    dvdt[1:-1] = __g(u[1:-1], v[1:-1], p, q) + Dv * np.diff(v, 2) / dx ** 2
    dvdt[-1] = __g(u[-1], v[-1], p, q) + Dv * (-2.0 * v[-1] + 2.0 * v[-2]) / dx ** 2

    return dydt
