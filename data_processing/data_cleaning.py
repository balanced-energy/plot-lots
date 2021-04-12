import pandas as pd
import re

# Create DataFrame
filename = 'data/location_data.csv'
df = pd.read_csv(filename)


# Data Cleaning
# Drop NA data for map
df = df.dropna(subset=['Full Address'])
df = df.dropna(subset=['point'])


# REGEX
# Match pattern to capture acreage pattern
# (.)[0-9] followed by optional spaces then "AC", "Acres", "AC"
def split_acres(s):
    pattern = r'(\d*\.?\d+\s?)(?=AC|Ac|ac)'
    # Return matching acreage values in acrs_list
    acres_list = re.findall(pattern, s)
    # Find max acreage and check if acres_list exists else 0
    acr_max = max(acres_list, key=lambda x: float(x))\
        if acres_list else 0
    return acr_max


# Split off Acreage from 'Legal Description' series
df['Size'] = df['Legal Description'].apply(
    lambda x: split_acres(x)
)


# Creat Hover_info for map, Size and minimum bid
df['Hover_info'] = df['Size'].astype(str) \
                   + ' -- AC, BID: ' \
                   + df['Minimum Bid'].astype(str)


# Save file
df.to_csv(r'data/final_data.csv', index = False, header=True)

print("Created -- final_data.csv")
