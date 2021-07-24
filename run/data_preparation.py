from geopy.geocoders import GoogleV3
import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
# Google Maps API Key
API_KEY = "AIzaSyBU3_-Q4L939MaSJvbkY_skYmewagYKhPE"

# Instantiate locator
locator = GoogleV3(api_key=API_KEY)

# Set delay between geocoding calls
geocode = RateLimiter(locator.geocode, min_delay_seconds=.5)

# Read in file
# Requirements: File must be name 'original_data.xlsx'
# Notes: Excel file type
# Read in file and create DataFrame
filename = 'data/original_data.csv'
df = pd.read_csv(filename)

# Combine Property Address, City, Zip to new "Full Address" column
# Drop any NA values
df['Full Address'] = df[df.columns[3:6]].apply(
    lambda x: ', '.join(x.dropna().astype(str)),
    axis=1
)

# API REQUEST - Data Retrieval
# Query location run for "Full Address" series
# Create 'location' column to store point (tuple) values
print("API Request...In Progress")
df['location'] = df['Full Address'].apply(locator.geocode)

# Must be done before saving csv file, otherwise location.point run lost
# Create point - latitude, longitude values
df["point"] = df["location"].apply(lambda loc: tuple(loc.point) if loc else None)
# Extract lat, lon, alt values
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].to_list(), index=df.index)


# Save file
df.to_csv(r'run/location_data.csv', index = False, header=True)

print("Created -- location_data.csv")

