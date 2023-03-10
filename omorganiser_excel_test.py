import openpyxl

# Laster inn excelfil
wb = openpyxl.load_workbook('rearrange.xlsx')
ws = wb.active

# Sjekker antall kolonner i arket
num_cols = ws.max_column

# Sletter rader baklengs fra AD til A hvis det er mer enn 5 kolonner
if num_cols > 5:
    for col in range(30, 0, -1):
        print(col)
        ws.delete_cols(col)
        
    else:
        print("Det er for få kolonner i filen")

# Lagrer endringer til en annen excelfil 
wb.save('file2.xlsx')
