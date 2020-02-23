import re
import numpy as np
from typing import Dict, Any
from Analyze.Glycolysis1d.Result import Result


def preprocess_string_saved_by_np(string: str) -> str:
    return re.sub('[\\s]+', ',', string[1:-1])


def calc_picks(points: np.ndarray, key_suffix: str) -> Dict[str, Any]:
    derivative_sign = 1 if points[2] - points[1] >= 0 else -1
    half_picks = 0
    for i in range(2, len(points) - 3):
        if (points[i + 1] - points[i]) / derivative_sign < 0:
            derivative_sign *= -1
            half_picks += 1
    return {'picks_{0}'.format(key_suffix): half_picks / 2 + (0.5 if half_picks > 0 else 0),
            'direction_{0}'.format(key_suffix): 'down' if derivative_sign < 0 else 'up'}


def add_picks_analysis_to_meta(res: Result) -> None:
    current = calc_picks(res.meta['res_u'], 'res_u')
    for key in current:
        assert key not in res.meta
    res.meta.update(current)
    current = calc_picks(res.meta['res_v'], 'res_v')
    for key in current:
        assert key not in res.meta
    res.meta.update(current)
