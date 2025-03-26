import pandas as pd

CJFM_2020 = pd.read_csv('../datasets/MTA_B2020_CJFM.csv')
CJFM_2025 = pd.read_csv('../datasets/MTA_B2025_CJFM.csv')
OTPM_2020 = pd.read_csv('../datasets/MTA_B2020_OTPM.csv')
OTPM_2025 = pd.read_csv('../datasets/MTA_B2025_OTPM.csv')

CJFM_2020 = CJFM_2020.drop('division', axis=1)
CJFM_2025 = CJFM_2025.drop('division', axis=1)
OTPM_2020 = OTPM_2020.drop('division', axis=1)
OTPM_2025 = OTPM_2025.drop('division', axis=1)

deinterlined = CJFM_2020[CJFM_2020['line'].isin([
                                                    '1',
                                                    '6',
                                                    '7',
                                                    'G',
                                                    'L',
                                                    'S 42nd',
                                                    'S Fkln',
                                                    'S Rock'])]
interlined = CJFM_2020[~CJFM_2020['line'].isin([
                                                    '1',
                                                    '6,'
                                                    '7',
                                                    'G',
                                                    'L',
                                                    'S 42nd',
                                                    'S Fkln',
                                                    'S Rock'])]
current_deinterlined = CJFM_2025[CJFM_2025['line'].isin([
                                                    '1',
                                                    '6',
                                                    '7',
                                                    'G',
                                                    'L',
                                                    'S 42nd',
                                                    'S Fkln',
                                                    'S Rock'])]
current_interlined = CJFM_2025[~CJFM_2025['line'].isin([
                                                    '1',
                                                    '6,'
                                                    '7',
                                                    'G',
                                                    'L',
                                                    'S 42nd',
                                                    'S Fkln',
                                                    'S Rock'])]

print(deinterlined)