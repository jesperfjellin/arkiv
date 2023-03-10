import os
import glob
import subprocess

# Set the directory path where the folders are located
dir_path = r"Y:\Kartografi\N50_Kartdata\Arbeidsfiler\FKBdata\endringsdata"

# Find the first folder that starts with "omr02_" in the directory
folders = glob.glob(os.path.join(dir_path, "omr02_*"))
if len(folders) == 0:
    print("No folders found starting with 'omr02_' in the directory.")
    exit()
first_folder = folders[0]

# Set the path to the ArcGIS Pro executable
arcgis_pro_path = r"C:\Program Files\ArcGIS\Pro\bin\ArcGISPro.exe"

# Set the path to the GDB file you want to add to the map
gdb_file_path = os.path.join(first_folder, "FKB_ENDRING.gdb")

# Open ArcGIS Pro and add the GDB file to the map
subprocess.Popen([arcgis_pro_path, gdb_file_path])