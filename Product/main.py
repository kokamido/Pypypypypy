from Product.Glycolysis1D.Experiment import *
import numpy as np
import os


initCond = InitCond1dSettings('rand', 0.1, 200, 0)
systemSettings = GlycolysisSettings(3,1,7,1,0.2)

for Du in [7,10,20]:
    systemSettings.Du = Du
    for j in range(1000):
        path = 'C:\\Users\\alexandr.pankratov\\bashkirtseva\\distr'
        if os.path.exists(path+'\\2020-03-17\\'+str(Du)+'_'+str(j)) or os.path.exists(path+'\\2020-03-18\\'+str(Du)+'_'+str(j)):
            print('skip '+str(Du)+'_'+str(j))
            continue
        try:
            run_experiment(str(Du)+'_'+str(j), initCond,systemSettings,0,5000,0.01,1e-3,path)
        except:
            run_experiment(str(Du)+'_'+str(j), initCond,systemSettings,0,5000,0.01,1e-3,path)