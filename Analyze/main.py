import os
from datetime import datetime

import pandas as pd

from Analyze.Glycolysis1d.PatternAnalyzeHelper import add_picks_analysis_to_meta
from Analyze.Glycolysis1d.Result import ResultHiggins

base_directory = 'C:\\Users\\alexandr.pankratov\\math_newest\\2020-02-02'

results = []
for subdir in os.listdir(base_directory):
    full_path = os.path.join(base_directory, subdir)
    if not os.path.isdir(full_path):
        continue
    current = ResultHiggins(full_path)
    add_picks_analysis_to_meta(current)
    row = current.make_row_and_exclude_np_arrays()
    results.append(row)

pd.DataFrame(results).to_csv(os.path.join(base_directory, '_res_' + str(datetime.now()).replace(':', '_')))
