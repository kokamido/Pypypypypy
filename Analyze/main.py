import os
from datetime import datetime

import pandas as pd

from Analyze.Glycolysis1d.PatternAnalyzeHelper import add_picks_analysis_to_meta
from Analyze.Glycolysis1d.Result import ResultHiggins

base_directory = 'C:\\Users\\alexandr.pankratov\\Desktop\\pravki\\data2'

results = []
for subdirr in os.listdir(base_directory):
    for subdir in os.listdir(os.path.join(base_directory, subdirr)):
        full_path = os.path.join(base_directory, subdirr, subdir)
        if not os.path.isdir(full_path):
            continue
        current = ResultHiggins(full_path)
        add_picks_analysis_to_meta(current)
        row = current.make_row_and_exclude_np_arrays()
        results.append(row)

pd.DataFrame(results).to_csv(os.path.join(base_directory, '_res_' + str(datetime.now()).replace(':', '_')))
