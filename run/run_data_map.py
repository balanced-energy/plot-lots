
# Automate running run preparation and map creation files
# Note: Only run data_preparation file first time  to query api
#       and save longitude, latitude locations to location_data
# exec(open('./data_preparation.py').read())
exec(open('./data_cleaning.py').read())
exec(open('./folium_map.py').read())
