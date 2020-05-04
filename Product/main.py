from Product.Glycolysis1D.Experiment import *
import numpy as np
from pylab import rcParams
import os

from Product.Glycolysis1D.Glycolysis import run_higgins_0d

systemSettings = GlycolysisSettings(3, 1, 20, 1, 0.2)
initCond = InitCondSettings()
initCond.points_count = 200
initCond.values = np.ones(400)
u = initCond.values[::2]
v = initCond.values[1::2]
u*=0.25970648
v*=3.40284572
rand = np.random.rand(100)*0.05
u[0:100]+=rand
u[100:]+=rand[::-1]
v[0:100]+=rand
v[100:]+=rand[::-1]
u[0]=u[1]
u[-1]=u[-2]
v[0]=v[1]
v[-1]=v[-2]
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
run_experiment(str(systemSettings.Du), initCond, systemSettings, 0, 5000, 0.01, 3e-4,'C:\\Users\\alexandr.pankratov\\bashkirtseva\\noisy20_19_04_2020', True,transient_save_step=0.1)

