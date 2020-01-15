from Experiment import *
import os
import random

init_cond = InitCond1dSettings('rand', 0.5, 400, 3.5)
params = GlycolysisSettings(3, 1, 20, 1, 0.1)
for patt in ['rand', 'cos']:
    for pcks in np.arange(0.5, 20.5, 0.5):
        init_cond.pattern_type = patt
        init_cond.picks_count = pcks
        run_experiment(str(datetime.now()), init_cond, params, 0, 1000, 0.01,
                       path_to_save=os.path.join(os.path.expanduser('~'), 'math'), save_transient=False, tolerance=1e-4)
