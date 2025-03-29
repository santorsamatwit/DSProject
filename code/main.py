import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def arr_averager(a):
    for i in range(0,len(a)):
        a[i] = a[i].mean()

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

# creates an array out of the numerical values from the data, ignoring line letterings and numbers

deinterlined_arr = np.array([deinterlined['additional platform time'], deinterlined['additional train time'], deinterlined['total_apt'], deinterlined['total_att'], deinterlined['over_five_mins'], deinterlined['over_five_mins_perc']])

interlined_arr = np.array([interlined['additional platform time'], interlined['additional train time'], interlined['total_apt'], interlined['total_att'], interlined['over_five_mins'], interlined['over_five_mins_perc']])

# creates an array out of deinterlined and interlined of the averages of every numerical value, rounded to 3 places.

avg_deinterlined_arr = np.round(np.mean(deinterlined_arr),3)
avg_interlined_arr = np.round(np.mean(interlined_arr),3)

averaged_sample_size = int((len(deinterlined_arr[0]) + len(interlined_arr[0])) / 2)
