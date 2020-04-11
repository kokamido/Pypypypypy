from Product.Glycolysis1D.Experiment import *
import numpy as np
from pylab import rcParams
import os

from Product.Glycolysis1D.Glycolysis import run_higgins_0d

systemSettings = GlycolysisSettings(3, 1, 10, 1, 0.2)

dx = 0.2
x_max = 40
points_count = int(x_max / dx)

points_from_cycle = {0.3: [0.13392937, 7.36221299], 0.4: [2.08160866, 1.13180034e-03], 0.5: [1.55676445, 0.03172123],
                     0.6: [1.62100812, 0.04337005], 0.7: [0.71812875, 7.47688964], 0.8: [0.20905959, 4.42663615],
                     0.9: [0.24221072, 3.70282509], 1.0: [0.87859153, 0.46305174], 1.1: [0.42667616, 1.71194896],
                     1.2: [0.29618477, 3.68680293], 1.3: [0.59590443, 0.99281201], 1.4: [0.92362164, 0.45655522],
                     1.5: [1.6325804, 0.38814785], 1.6: [0.62885128, 1.0310077], 1.7: [0.85392662, 0.64045561],
                     1.8: [0.63948281, 1.82462986], 1.9: [1.07090892, 0.62412627], 2.0: [1.00918232, 0.92540534]}

init = InitCondSettings()
init.values = np.ones(points_count * 2)
init.points_count = points_count
rand = np.random.rand(points_count) * 0.5
#rand[0] = rand[1]
half_points_count = int(points_count / 2)
rand[half_points_count:] = rand[half_points_count - 1::-1]
u = init.values[::2]
u *= 0.25970648
#u *= points_from_cycle[q][0]
u += rand
u[0] = u[1]
u[-1] = u[-2]
v = init.values[1::2]
v *= 3.40284572
#v *= points_from_cycle[q][1]
v += rand
v[0] = v[1]
v[-1] = v[-2]
run_experiment('noisy '+str(systemSettings.Du), init, systemSettings, 0, 100, 0.001, 1e-3,'C:\\Users\\alexandr.pankratov\\Desktop\\Свежие картнки', True,transient_save_step=0.01)
