import pandas as pd
import geopandas as gpd
import shapely.wkt as wkt
import csv
import os
import sys
import shutil

csv.field_size_limit(1000000)

try:
    df = pd.read_csv('parlinjer.csv', delimiter="\t", header=None, names=['wkt'])
except FileNotFoundError:
    print("Error: new_geometry.csv not found.")
    sys.exit()

df['geometry'] = df['wkt'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry='geometry')
gdf.crs = 'epsg:25833'

filename = 'C:/Kartografi_Jesper/Python/veger_under_konstruksjon/new_geometry.shp'
if os.path.isfile(filename):
    print("Warning: Existing file has been overwritten:", filename)

gdf.to_file(filename, driver='ESRI Shapefile')

# Delete the "data.csv" and "data_cleaned.csv" files
if os.path.isfile('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data.csv'):
    os.remove('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data.csv')
cleaned_file = 'C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_cleaned.csv'
if os.path.isfile(cleaned_file):
    if os.path.isfile('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_cleaned_original.csv'):
        os.remove('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_cleaned_original.csv')
    shutil.move(cleaned_file, 'C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_cleaned_original.csv')
