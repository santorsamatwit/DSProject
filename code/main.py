import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def arr_averager(a):
    for i in range(0,len(a)):
        a[i] = a[i].mean()

DEINTERLINED_PATHS = {
    '7S': '7-S-701-726'
    '7N': '7-N-726-701'
}
INTERLINED_PATHS = {

}

# dataset importing
DATASET = pd.read_csv('../datasets/MTA_EtoE_Times.csv')

print(DATASET)

# dataset cleaning
DATASET = DATASET.drop(['Time Period','Schedule Day Type','Average Speed', 'Average Scheduled Runtime', 'Scheduled Trains', 'Actual Trains', 'Distance', 'Direction', 'Number of Stops', 'Origin Station Name', 'Origin Station ID', 'Destination Station Name', 'Destination Station ID',], axis=1)



print(DATASET)