import openpyxl
import pandas as pd

# Laster inn excelfil
wb = openpyxl.load_workbook('rearrange.xlsx')
ws = wb.active

# Sletter rader baklengs fra AD til A
for col in range(30, 0, -1):
    ws.delete_cols(col)
print("Kolonner har blitt slettet.")   

# Lagrer endringer til en annen excelfil 
wb.save('file2.xlsx')

# Leser inn den nye excelfilen
df = pd.read_excel('file2.xlsx')

# Konverterer til CSV
df.to_csv('file2.csv', index=False)

print("CSV-fil er lagret.")
