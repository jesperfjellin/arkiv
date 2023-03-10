import pandas as pd

# Read in the file using pandas
df = pd.read_csv('delimiter1.csv', sep='\t', header=None, names=['wkt'])

# Display the dataframe
print(df)
