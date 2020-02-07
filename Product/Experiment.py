from Product.Glycolysis import GlycolysisSettings, run
from Product.InitCond1dSettings import InitCond1dSettings
from Product.MathHelper import calc_difference
from Product.DrawHelper import draw_values
from typing import Dict, Any
import numpy as np
from matplotlib import rcParams
from matplotlib import pylab as plt
from datetime import datetime
import logging
import json
import os

logger = logging.getLogger('experiment_{0}'.format(datetime.now()))
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def set_rc_params_for_1d_patterns():
    logger.debug('Setting up rcParams for 1d patterns')
    rcParams['figure.figsize'] = 10, 10
    rcParams['legend.fontsize'] = 14
    rcParams['axes.titlesize'] = 18
    rcParams['xtick.labelsize'] = 14
    rcParams['ytick.labelsize'] = 14
    rcParams['grid.color'] = 'black'


def run_experiment(id_: str, init_pattern: InitCond1dSettings, params: GlycolysisSettings, t0: float, t1: float,
                   dt: float, tolerance: float = 1e-5, path_to_save: str = None, save_transient: bool = False,
                   transient_save_step: float = 0.1) -> \
        Dict[str, Any]:
    logger.info('Start experiment with id:\'{0}\'\ninit: conditions \'{1}\'\nparams: \'{2}\''
                .format(id_, str(init_pattern), str(params)))
    init_curve = current_pattern = init_pattern.calc_values()
    delta = 999999
    result = {'init': init_pattern.to_dict(),
              'init_pattern': init_curve,
              'params': params.to_dict(),
              'method_params':{'dt':dt, 'tolerance':tolerance,'transient save step':transient_save_step}}
    if save_transient:
        process = np.array([current_pattern])
    step = 0
    t_start = t0
    t_end = t0 + dt * 10000
    transient_save_step = int(transient_save_step / dt)
    iters_to_check_stability = 10
    while iters_to_check_stability > 0 and t_end < t1:
        step += 1
        new_patterns, meta = run(params, np.arange(t_start, t_end, dt), current_pattern)
        if meta['message'] != 'Integration successful.':
            raise Exception(meta['message'])
        delta = calc_difference(current_pattern, new_patterns[-1])
        current_pattern = new_patterns[-1]
        if save_transient:
            process = np.concatenate((process, new_patterns[::transient_save_step]))
        del new_patterns
        logger.debug('delta after step {0} is {1}'.format(step, delta))
        t_start = t_end
        t_end += dt * 10000
        if delta < tolerance:
            logger.debug('Stability checking, delta after step {0} is {1}'.format(step, delta))
            iters_to_check_stability -= 1
        else:
            iters_to_check_stability = 10
    result['method_params']['max_time'] = t_start

    result['end_pattern'] = current_pattern
    if delta < tolerance:
        
        logger.info('Experiment with id \'{0}\' has been successfully finished'.format(id_))
    else:
        logger.info('Experiment with id \'{0}\' has been failed'.format(id_))

    if path_to_save:
        set_rc_params_for_1d_patterns()
        dir_to_save = os.path.join(path_to_save, str(datetime.now().date()).replace(':', '_'), str(id_))
        logger.info('Saving results to \'{0}\''.format(dir_to_save))
        if not os.path.exists(dir_to_save):
            os.makedirs(dir_to_save)
        result['init_pattern'] = np.array2string(result['init_pattern'], threshold=init_pattern.points_count * 2,
                                                 max_line_width=100000)
        result['end_pattern'] = np.array2string(result['end_pattern'], threshold=init_pattern.points_count * 2,
                                                max_line_width=100000)
        logger.debug('Drawing')
        draw_data = draw_values(init_curve, params.dx, labels=('init_u', 'init_v'))
        draw_values(current_pattern, params.dx, titles=('u', 'v'), labels=('u', 'v'), draw_data=draw_data)
        plt.savefig(dir_to_save + '/result.png')

        logger.debug('Saving meta')
        with open(dir_to_save + '/meta.json', 'w') as out:
            out.write(json.dumps(result, indent=1))

        if save_transient:
            logger.debug('Saving process')
            with open(dir_to_save + '/process', 'w') as out:
                np.savetxt(out, process, fmt='%.6f', delimiter=',')
    elif save_transient:
        result['process'] = process
    logger.info('Data has been saved')
    return result
