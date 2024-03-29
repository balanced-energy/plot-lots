import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Read and populate dataframe
csv_file = 'data/final_data.csv'
df = pd.read_csv(csv_file)

# Initialize folium map
m = folium.Map(location=df[["latitude", "longitude"]].mean().to_list(), zoom_start=15)
#m = folium.Map(location=df[["latitude", "longitude"]])

# # Test default zoom
# sw = df[["latitude", "longitude"]].min().values.tolist()
# ne = df[["latitude", "longitude"]].max().values.tolist()
#
# m.fit_bounds([sw, ne])
# Cluster close points, create a cluster overlay with MarkerCluster, add to m
marker_cluster = MarkerCluster().add_to(m)

# Create marks and assign popup and tooltip values
# Add markets to the cluster
for i, r in df.iterrows():
    location = (r["latitude"], r["longitude"])
    folium.Marker(location=location,
                      popup = r['Full Address'],
                      tooltip=r['Hover_info'])\
        .add_to(marker_cluster)


# Create index.html file
m.save('../templates/apps/index.html')
print("Updated map HTML")
