from typing import Any, Dict

import numpy as np


class InitCond1dSettings:
    pattern_type: str = None
    amp: float = None
    points_count: int = None
    picks_count: float = None

    def __init__(self, pattern_type: str, amp: float, points_count: int, picks_count: float):
        self.pattern_type = pattern_type
        self.amp = amp
        self.points_count = points_count
        self.picks_count = picks_count

    def calc_values(self):
        assert self.amp is not None
        assert self.points_count is not None
        if self.pattern_type is None or self.pattern_type == 'rand':
            return self.__get_init_values_rand()
        if self.pattern_type == 'cos':
            assert self.points_count is not None
            return self.__get_init_values_cos()

    def __get_init_values_rand(self) -> np.ndarray:
        u = np.random.rand(self.points_count) * self.amp + 1
        v = np.random.rand(self.points_count) * self.amp + 1
        res = np.zeros(self.points_count * 2, dtype=np.float)
        res[::2] = u
        res[1::2] = v
        u[0] = u[1]
        v[0] = v[1]
        u[-1] = u[-2]
        v[-1] = v[-2]
        return res

    def __get_init_values_cos(self) -> np.ndarray:
        u = np.cos(np.linspace(0, 2 * np.pi * self.picks_count, self.points_count))
        v = np.cos(np.linspace(0, 2 * np.pi * self.picks_count, self.points_count))
        res = np.zeros(self.points_count * 2, dtype=np.float)
        res[::2] = u
        res[1::2] = v
        return res * self.amp + 1

    def to_dict(self) -> Dict[str, Any]:
        return {
            'pattern_type': self.pattern_type,
            'amp': self.amp,
            'points_count': self.points_count,
            'picks_count': self.picks_count
        }

    def __to_str(self) -> str:
        return str(self.to_dict())

    def __str__(self):
        return self.__to_str()

    def __repr__(self):
        return self.__to_str()
