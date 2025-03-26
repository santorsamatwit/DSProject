import pandas as pd
import numpy as np
import matplotlib as mpl

# dataset importing
CJFM_2020 = pd.read_csv('../datasets/MTA_B2020_CJFM.csv')
CJFM_2025 = pd.read_csv('../datasets/MTA_B2025_CJFM.csv')
OTPM_2020 = pd.read_csv('../datasets/MTA_B2020_OTPM.csv')
OTPM_2025 = pd.read_csv('../datasets/MTA_B2025_OTPM.csv')


# data cleaning
CJFM_2020 = CJFM_2020.drop('division', axis=1)
CJFM_2025 = CJFM_2025.drop('division', axis=1)
OTPM_2020 = OTPM_2020.drop('division', axis=1)
OTPM_2025 = OTPM_2025.drop('division', axis=1)

# data sorting
deinterlined = CJFM_2020[CJFM_2020['line'].isin(['1', '6', '7', 'G', 'L', 'S 42nd', 'S Fkln', 'S Rock'])]
interlined = CJFM_2020[~CJFM_2020['line'].isin(['1', '6', '7', 'G', 'L', 'S 42nd', 'S Fkln','S Rock'])]

current_deinterlined = CJFM_2025[CJFM_2025['line'].isin(['1', '6', '7', 'G', 'L', 'S 42nd', 'S Fkln', 'S Rock'])]
current_interlined = CJFM_2025[~CJFM_2025['line'].isin(['1', '6', '7', 'G', 'L', 'S 42nd', 'S Fkln', 'S Rock'])]

otpm = OTPM_2020[OTPM_2020['line'].isin(['1', '6', '7', 'G', 'L', 'S 42nd', 'S Fkln', 'S Rock'])]
current_otpm = OTPM_2020[OTPM_2020['line'].isin(['1', '6', '7', 'G', 'L', 'S 42nd', 'S Fkln','S Rock'])]

# creates an array out of deinterlined and interlined of the averages of every numerical value, rounded to 3 places.
avg_deinterlined_arr = np.round(np.array([deinterlined['additional platform time'].mean(), deinterlined['additional train time'].mean(), deinterlined['total_apt'].mean(), deinterlined['total_att'].mean(), deinterlined['over_five_mins'].mean(), deinterlined['over_five_mins_perc'].mean()]),3)
avg_interlined_arr = np.round(np.array([interlined['additional platform time'].mean(), interlined['additional train time'].mean(), interlined['total_apt'].mean(), interlined['total_att'].mean(), interlined['over_five_mins'].mean(), interlined['over_five_mins_perc'].mean()]),3)



print(avg_deinterlined_arr)