from Product.Glycolysis1D.Experiment import *
import numpy as np
from pylab import rcParams
import os

from Product.Glycolysis1D.Glycolysis import run_higgins_0d

systemSettings = GlycolysisSettings(3, 1, 7, 1, 0.2)
initCond = InitCondSettings()
'''
"init": {
  "pattern_type": "rand",
  "amp": 0.1,
  "points_count": 200,
  "picks_count": 0
 },
 "params": {
  "p": 3,
  "q": 1,
  "Du": 7,
  "Dv": 1,
  "dx": 0.2
 },
 "method_params": {
  "dt": 0.01,
  "tolerance": 0.001,
  "transient save step": 0.1,
  "max_time": 4900.0
 },
 '''
j = 0
for i in ['C:\\Users\\alexandr.pankratov\\Desktop\\pravki\\data2\\2020-04-17\\159_7',
'C:\\Users\\alexandr.pankratov\\Desktop\\pravki\\data2\\2020-04-17\\227_7',
'C:\\Users\\alexandr.pankratov\\Desktop\\pravki\\data2\\2020-04-17\\358_7',
'C:\\Users\\alexandr.pankratov\\Desktop\\pravki\\data2\\2020-04-17\\420_7',
'C:\\Users\\alexandr.pankratov\\Desktop\\pravki\\data2\\2020-04-17\\441_7']:
    initCond.init_from_meta(i)
    run_experiment(str(j)+'_'+str(systemSettings.Du), initCond, systemSettings, 0, 5000, 0.01, 1e-5,'C:\\Users\\alexandr.pankratov\\Desktop\\pravki\\data3_5wtf', True,transient_save_step=0.1)
    j+=1