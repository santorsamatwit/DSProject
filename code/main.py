import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def arr_averager(a):
    for i in range(0,len(a)):
        a[i] = a[i].mean()

DEINTERLINED_TERMINI = {

    '1': ['VAN CORTLANDT PARK-242 ST', 'SOUTH FERRY'],
    '6': ['PELHAM BAY PARK', 'BKLYN BRIDGE CITY HALL'],
    '7': ['34TH ST HUDSON YARDS', 'FLUSHING-MAIN ST'],
    'G': ['COURT SQ', 'CHURCH AV'],
    'L': ['14 ST', '8 AV'],
    'S42': ['TIMES SQ 42 ST', 'GRAND CENTRAL 42 ST'],
    'SF': ['FRANKLIN AV', 'PROSPECT PARK'],
    'SR': ['BROAD CHANNEL', 'ROCKAWAY PARK-BEACH 116 ST']
}
INTERLINED_TERMINI = {
    '2': ['WAKEFIELD-241 ST', 'FLATBUSH AV-BROOKLYN COLLEGE'],
    '3': ['HARLEM 148 ST', 'NEW LOTS AV'],
    '4': ['WOODLAWN', 'CROWN HEIGHTS-UTICA AV'],
    '5': ['EASTCHESTER-DYRE AV', 'FLATBUSH AV-BROOKLYN COLLEGE'],
    'A': ['INWOOD 207 ST', 'OZONE PARK-LEFFERTS BLVD', 'FAR ROCKAWAY MOTT AV', 'ROCKAWAY PARK-BEACH 116 ST'],
    'C': ['168 ST', 'EUCLID AV'],
    'E': ['JAMAICA CENTER-PARSONS/ARCHER', 'WORLD TRADE CENTER'],
    'B': ['BEDFORD PK BLVD', 'BRIGHTON BEACH'],
    'D': ['NORWOOD 205 ST', 'STILLWELL AV'],
    'F': [],
    'M': [],
    'N': [],
    'R': [],
    'Q': [],
    'W': [],
    'J': [],
    'Z': []
}

# dataset importing
DATASET = pd.read_csv('../datasets/MTA_EtoE_Times.csv')

print(DATASET)

# dataset cleaning
DATASET = DATASET.drop(['Time Period','Schedule Day Type','Average Speed', 'Average Scheduled Runtime', 'Scheduled Trains', 'Actual Trains', 'Distance', 'Direction', 'Number of Stops', 'Stop Path ID' 'Origin Station ID', 'Destination Station ID',], axis=1)



print(DATASET)