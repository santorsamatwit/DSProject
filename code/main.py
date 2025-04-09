import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
pd.options.mode.chained_assignment = None

def arr_averager(a):
    for i in range(0,len(a)):
        a[i] = a[i].mean()

def find_fastest_line(line_dfs):
    fastest_line = None
    fastest_avg_runtime = float('inf')

    for line, df in line_dfs.items():
        if not df.empty and 'Average Actual Runtime' in df.columns:
            avg_runtime = df['Average Actual Runtime'].mean()
            if avg_runtime < fastest_avg_runtime:
                fastest_avg_runtime = avg_runtime
                fastest_line = line
        elif df.empty:
            print(f"Warning: No data available for line {line} to calculate average runtime.")
        else:
            print(f"Warning: 'Average Actual Runtime' column not found for line {line}.")

    if fastest_line:
        print(f"The fastest line on average is line {fastest_line} with an average actual runtime of {fastest_avg_runtime:.2f} in minutes.")
    else:
        print("No line data available with 'Average Actual Runtime' to determine the fastest line.")
    return fastest_line, fastest_avg_runtime

def analyze_speed_trend(line_dfs, category_name):
    fastest_line = None
    fastest_avg_runtime = float('inf')
    trends = {}

    for line, df in line_dfs.items():
        if not df.empty and 'Average Actual Runtime' in df.columns and 'Month' in df.columns:
            try:
                # Ensure 'Month' is treated as a numerical category
                df['Month_numeric'] = pd.to_datetime(df['Month'],format='%m/01/%Y', errors='coerce').dt.month
                df_cleaned = df.dropna(subset=['Month_numeric', 'Average Actual Runtime'])

                if not df_cleaned.empty:
                    X = df_cleaned['Month_numeric'].values.reshape(-1, 1)
                    y = df_cleaned['Average Actual Runtime'].values
                    model = LinearRegression()
                    model.fit(X, y)
                    slope = model.coef_[0]
                    intercept = model.intercept_

                    # Get the last month and corresponding runtime
                    last_month = df_cleaned['Month_numeric'].iloc[-1]
                    last_avg_runtime = df_cleaned['Average Actual Runtime'].iloc[-1]

                    trends[line] = {'slope': slope, 'intercept': intercept, 'last_month': last_month, 'last_avg_runtime': last_avg_runtime}

                    current_avg_runtime = df_cleaned['Average Actual Runtime'].mean()
                    if current_avg_runtime < fastest_avg_runtime:
                        fastest_avg_runtime = current_avg_runtime
                        fastest_line = line
                else:
                    print(f"Warning: Not enough valid data (Month and runtime) for linear regression on {category_name} line {line}.")

            except Exception as e:
                print(f"Error during linear regression for {category_name} line {line}: {e}")
        elif df.empty:
            print(f"Warning: No data available for {category_name} line {line}.")
        else:
            print(f"Warning: Missing required columns ('Average Actual Runtime' or 'Month') for {category_name} line {line}.")

    print(f"\n--- Speed Trend Analysis (using 'Month' column) for {category_name} Lines ---")
    fastest_line_future_prediction = None
    fastest_future_runtime = float('inf')

    if fastest_line and trends:
        print(f"\nCurrent fastest {category_name} line (based on overall average): {fastest_line} (Average Actual Runtime: {fastest_avg_runtime:.2f})")

        for line, trend in trends.items():
            slope = trend['slope']
            intercept = trend['intercept']
            last_month = trend['last_month']
            last_avg_runtime = trend['last_avg_runtime']
            trend_desc = "slowing down" if slope > 0 else "speeding up" if slope < 0 else "staying relatively constant"
            print(f"Line {line}: Trend (per month): {trend_desc} (Slope: {slope:.8e}, Last Avg Runtime: {last_avg_runtime:.2f})")

            # Projecting to the next month (assuming monthly data)
            future_month = last_month + 1
            future_runtime = slope * future_month + intercept

            if future_runtime < fastest_future_runtime:
                fastest_future_runtime = future_runtime
                fastest_line_future_prediction = line

        if fastest_line_future_prediction:
            print(f"\nBased on linear regression, the fastest {category_name} line in the next month (projected) might be: {fastest_line_future_prediction} (Projected Average Actual Runtime: {fastest_future_runtime:.2f})")
            if fastest_line_future_prediction == fastest_line:
                print(f"This suggests that the current fastest {category_name} line ({fastest_line}) is likely to remain the fastest.")
            else:
                print(f"This suggests a potential change in the fastest {category_name} line.")
        else:
            print(f"Could not predict the future fastest {category_name} line.")

    else:
        print(f"Could not determine the current fastest {category_name} line or analyze trends.")





DEINTERLINED_TERMINI = {
    '1': ['242ND STREET-BWAY', 'SOUTH FERRY TERMINAL'], #
    '6': ['PELHAM BAY PARK', 'BROOKLYN BRIDGE'], # 6 exp and 6 loc have the same termini, just fewer stops on exp
    '7': ['34TH STREET-HUDSON YARDS', 'FLUSHING-MAIN STREET'], # 7 exp and 7 loc have the same termini, just fewer stops on exp
    'G': ['COURT SQUARE', 'CHURCH AVENUE'], #
    'GS': ['TIMES SQUARE-SHUTTLE', 'GRAND CENTRAL-SHUTTLE'], # may exclude as its a major outlier
    'FS': ['FRANKLIN AVENUE', 'PROSPECT PARK'], #
    'H': ['BROAD CHANNEL', 'BEACH 116TH STREET-ROCKAWAY PARK', 'ROCKAWAY BOULEVARD', 'MOTT AVENUE-FAR ROCKAWAY'] # still known as the H in the database
}
INTERLINED_TERMINI = {
    '2': ['EAST 241ST STREET', 'FLATBUSH AVENUE'], #
    '3': ['148TH STREET-LENOX', 'NEW LOTS AVENUE'], #
    '4': ['WOODLAWN-JEROME AVENUE', 'UTICA AVENUE'], #
    '5': ['DYRE AVENUE', 'FLATBUSH AVENUE', 'EAST 238TH STREET'], #
    'A': ['207TH STREET-8AV', 'LEFFERTS BOULEVARD-OZONE PARK', 'MOTT AVENUE-FAR ROCKAWAY', 'BEACH 116TH STREET-ROCKAWAY PARK'], #
    'C': ['168TH STREET-8AV', 'EUCLID AVENUE'], #
    'E': ['PARSONS/ARCHER-JAMAICA CENTER', 'WORLD TRADE CENTER'], #
    'B': ['BEDFORD PARK BLVD', 'BRIGHTON BEACH'], #
    'D': ['205TH STREET-NORWOOD', 'STILLWELL AVENUE-CONEY ISLAND'], #
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
DATASET = DATASET.drop(['Time Period', 'Schedule Day Type','Average Speed', 'Average Scheduled Runtime', 'Scheduled Trains', 'Actual Trains', 'Distance', 'Direction', 'Number of Stops', 'Stop Path ID', 'Origin Station ID', 'Destination Station ID',], axis=1)


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

deinterlined_ns_dataframes = deinterlined_dataframes.copy()
deinterlined_ns_dataframes.pop('GS')
deinterlined_ns_dataframes.pop('FS')
deinterlined_ns_dataframes.pop('H')


    
# Find the fastest deinterlined line
print("\n--- Fastest Deinterlined Line ---")
fastest_deinterlined_line, fastest_deinterlined_runtime = find_fastest_line(deinterlined_dataframes)

print("\n--- Fastest Deinterlined Line (no shuttles) ---")
fastest_deinterlined_ns_line, fastest_deinterlined_ns_runtime = find_fastest_line(deinterlined_ns_dataframes)

# Find the fastest interlined line
print("\n--- Fastest Interlined Line ---")
fastest_interlined_line, fastest_interlined_runtime = find_fastest_line(interlined_dataframes)


# Analyze deinterlined lines
analyze_speed_trend(deinterlined_dataframes, "Deinterlined")

analyze_speed_trend(deinterlined_ns_dataframes, "Deinterlined (No Shuttle)")

# Analyze interlined lines
analyze_speed_trend(interlined_dataframes, "Interlined")
