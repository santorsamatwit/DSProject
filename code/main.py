import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

def arr_averager(a):
    for i in range(0,len(a)):
        a[i] = a[i].mean()

DEINTERLINED_TERMINI = {
    '1': ['242ND ST-BWAY', 'SOUTH FERRY TERMINAL'], #
    '6': ['PELHAM BAY PARK', 'BROOKLYN BRIDGE'], # 6 exp and 6 loc have the same termini, just fewer stops on exp
    '7': ['34TH ST-HUDSON YARDS', 'FLUSHING-MAIN ST'], # 7 exp and 7 loc have the same termini, just fewer stops on exp
    'G': ['COURT SQUARE', 'CHURCH AVENUE'], #
    'L': ['14 ST', '8 AV'], # missing from dataset?
    'S42': ['TIMES SQUARE-SHUTTLE', 'GRAND CENTRAL-SHUTTLE'], # may exclude as its a major outlier
    'SF': ['FRANKLIN AVENUE', 'PROSPECT PARK'], #
    'H': ['BROAD CHANNEL', 'ROCKAWAY PARK-BEACH 116 ST', 'ROCKAWAY BLVD', 'MOTT AVENUE-FAR ROCKAWAY'] # still known as the H in the database
}
INTERLINED_TERMINI = {
    '2': ['EAST 241ST STREET', 'FLATBUSH AVENUE'], #
    '3': ['148TH STREET-LENOX', 'NEW LOTS AVENUE'], #
    '4': ['WOODLAWN-JEROME AVENUE', 'UTICA AVENUE'], #
    '5': ['DYRE AVENUE', 'FLATBUSH AVENUE', 'EAST 238TH STREET'], #
    'A': ['207 ST-8AV', 'LEFFERTS BOULEVARD-OZONE PARK', 'MOTT AVENUE-FAR ROCKAWAY', 'BEACH 116TH STREET-ROCKAWAY PARK'], #
    'C': ['168TH STREET-8AV', 'EUCLID AVENUE'], #
    'E': ['PARSONS/ARCHER-JAMAICA CENTER', 'WORLD TRADE CENTER'], #
    'B': ['BEDFORD PARK BLVD', 'BRIGHTON BEACH'], #
    'D': ['205 ST-NORWOOD', 'STILLWELL AVENUE-CONEY ISLAND'], #
    'F': ['179TH STREET-JAMAICA', 'STILLWELL AVENUE-CONEY ISLAND'], #
    'M': ['71ST/CONTINENTAL AVENUE-FOREST HILLS', 'METROPOLITAN AVENUE-MIDDLE VILLAGE'],
    'N': ['STILLWELL AVENUE-CONEY ISLAND', 'DITMARS BOULEVARD-ASTORIA', 'WHITEHALL STREET-SOUTH FERRY'], # W is an N short turn in the database
    'R': ['71ST/CONTINENTAL AVENUE-FOREST HILLS', '95TH STREET-BAY RIDGE'],
    'Q': ['STILLWELL AVENUE-CONEY ISLAND', '96TH STREET-2AV'],
    'J': ['PARSONS/ARCHER-JAMAICA CENTER', 'BROAD STREET'], # J and Z trips are the same, just some have fewer stops.
}

# dataset importing
DATASET = pd.read_csv('../datasets/MTA_EtoE_Times.csv')

# dataset cleaning
DATASET = DATASET.drop(['Time Period','Schedule Day Type','Average Speed', 'Average Scheduled Runtime', 'Scheduled Trains', 'Actual Trains', 'Distance', 'Direction', 'Number of Stops', 'Stop Path ID', 'Origin Station ID', 'Destination Station ID',], axis=1)


deinterlined_dataframes = {}
interlined_dataframes = {}

# Process deinterlined lines
for line, termini in DEINTERLINED_TERMINI.items():
    if len(termini) == 2:
        origin, destination = termini
        line_df = DATASET[((DATASET['Origin Station Name'] == origin) & (DATASET['Destination Station Name'] == destination)) |
                           ((DATASET['Origin Station Name'] == destination) & (DATASET['Destination Station Name'] == origin))]
        deinterlined_dataframes[line] = line_df
    elif len(termini) > 2:
        # Handle lines with multiple possible destinations (like the H line)
        conditions = []
        for i in range(len(termini)):
            for j in range(i + 1, len(termini)):
                origin, destination = termini[i], termini[j]
                conditions.append(((DATASET['Origin Station Name'] == origin) & (DATASET['Destination Station Name'] == destination)) |
                                  ((DATASET['Origin Station Name'] == destination) & (DATASET['Origin Station Name'] == origin)))
        if conditions:
            combined_condition = conditions[0]
            for condition in conditions[1:]:
                combined_condition = combined_condition | condition
            line_df = DATASET[combined_condition]
            deinterlined_dataframes[line] = line_df
        else:
            print(f"Warning: No termini pairs found for deinterlined line {line}")
    else:
        print(f"Warning: Invalid number of termini for deinterlined line {line}")

# Process interlined lines
for line, termini in INTERLINED_TERMINI.items():
    conditions = []
    # Handle lines with multiple possible termini
    for origin in termini:
        for destination in termini:
            if origin != destination:
                conditions.append(((DATASET['Origin Station Name'] == origin) & (DATASET['Destination Station Name'] == destination)) |
                                  ((DATASET['Origin Station Name'] == destination) & (DATASET['Origin Station Name'] == origin)))
    if conditions:
        combined_condition = conditions[0]
        for condition in conditions[1:]:
            combined_condition = combined_condition | condition
        line_df = DATASET[combined_condition]
        interlined_dataframes[line] = line_df
    else:
        print(f"Warning: No valid termini pairs found for interlined line {line}")


for line, df in deinterlined_dataframes.items():
    df.drop(['Origin Station Name', 'Destination Station Name'], axis=1, inplace=True)

for line, df in interlined_dataframes.items():
    df.drop(['Origin Station Name', 'Destination Station Name'], axis=1, inplace=True)

