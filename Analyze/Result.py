import os
import json
import numpy as np
from typing import Dict, Any
from Analyze import PatternAnalyzeHelper


class Result:
    process = None
    folder = None
    meta = None

    def get_process(self) -> np.ndarray:
        if self.process is None:
            self.process = np.loadtxt(os.path.join(self.folder, 'process'), dtype=np.ndarray)
        return self.process

    def make_row_and_exclude_np_arrays(self) -> Dict[str, Any]:
        res = {'folder': self.folder}
        for key in self.meta.keys():
            if isinstance(self.meta[key], np.ndarray):
                continue
            elif isinstance(self.meta[key], dict):
                for inner_key in self.meta[key].keys():
                    assert inner_key not in res
                res.update(self.meta[key])
            else:
                assert key not in res
                res[key] = self.meta[key]
        return res


class ResultHiggins(Result):

    def __init__(self, folder):
        self.folder = folder
        with open(os.path.join(folder, 'meta.json')) as inp:
            self.meta = json.load(inp)
        self.meta['init_pattern'] = np.fromstring(
            PatternAnalyzeHelper.preprocess_string_saved_by_np(self.meta['init_pattern']), dtype=np.float, sep=',')
        self.meta['init_u'] = np.array(self.meta['init_pattern'][::2], dtype=np.float)
        self.meta['init_v'] = np.array(self.meta['init_pattern'][1::2], dtype=np.float)

        self.meta['end_pattern'] = np.fromstring(
            PatternAnalyzeHelper.preprocess_string_saved_by_np(self.meta['end_pattern']), dtype=np.float, sep=',')
        self.meta['res_u'] = np.array(self.meta['end_pattern'][::2], dtype=np.float)
        self.meta['res_v'] = np.array(self.meta['end_pattern'][1::2], dtype=np.float)
