import os
import shutil
import pandas as pd

# Define the path of the source file
src_path = r'C:\Users\fjejes\Downloads\915_vegsystem-eksport.csv'

# Define the path of the destination folder
dst_folder = r'C:\\Kartografi_Jesper\\Python\\veger_under_konstruksjon\\'

# Create the destination folder if it doesn't exist
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

# Get the base filename of the source file
filename = os.path.basename(src_path)

# Define the path of the destination file
dst_path = os.path.join(dst_folder, filename)

# Cut and move the source file to the destination folder
shutil.move(src_path, dst_path)

# Rename the file to rearrange.xlsx
os.rename(dst_path, os.path.join(dst_folder, 'rearrange.csv'))

# Read in the CSV file
df = pd.read_csv('rearrange.csv', sep=';')

# Write the dataframe to an XLSX file
df.to_excel('rearrange.xlsx', index=False)
