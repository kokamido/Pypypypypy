from Product.Experiment import *
import os

init_cond = InitCond1dSettings('rand', 0.25, 1000, 3.5)
params = GlycolysisSettings(3, 1, 7, 1, 0.2)
for sas in [400]:
    for patt in ['rand', 'cos']:
        for pcks in np.arange(0.5, 20.5, 0.5):
            init_cond.pattern_type = patt
            init_cond.picks_count = pcks
            init_cond.points_count = sas
            run_experiment(str(datetime.now()).replace(':', '_'), init_cond, params, 0, 50000, 0.01,
                           path_to_save=os.path.join(os.path.expanduser('~'), 'math_newest'), save_transient=False,
                           tolerance=1e-3,transient_save_step=0.05)
