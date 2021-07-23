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
# [0-9]?,?[0-9]?(.)[0-9]
# followed by optional spaces and "AC", "Acres", "AC"
def split_acres(s):
    pattern = r'(\d*,?\d*\.?\d+\s?)(?=AC|Ac|ac)'
    acres = re.findall(pattern, s)
    if acres:
        size_max = max(acres, key=lambda x: float(x.replace(',', '')))
        return size_max + ' Acres'
    else:
        return 0


# Match pattern to capture acreage pattern
# [0-9]?,?[0-9]?(.)[0-9]
# followed by optional spaces and "SF", "Sf", "sf"
def split_sf(s):
    pattern = r'(\d*,?\d*\.?\d+\s?)(?=SF|Sf|sf)'
    sq_ft = re.findall(pattern, s)
    if sq_ft:
        size_max = max(sq_ft, key=lambda x: float(x.replace(',', '')))
        return size_max + ' Sf'
    else:
        return 0


# Split Size of acres or square ft off from String input
def split_size(s):
    if split_acres(s):
        return split_acres(s)
    else:
        return split_sf(s)


# Split off Size from 'Legal Description' series
df['Size'] = df['Legal Description'].apply(
    lambda x: split_size(x)
)

# Create Hover_info (Size, Minimum Bid)
df['Hover_info'] = df['Size'].astype(str) \
                   + ' --- MinBid: ' \
                   + df['Minimum Bid'].astype(str)


# Save file
df.to_csv(r'data/final_data.csv', index=False, header=True)

print("Created -- final_data.csv")
