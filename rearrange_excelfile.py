import openpyxl

# Load the excel file
wb = openpyxl.load_workbook('rearrange.xlsx')
ws = wb.active

# Delete columns A through AD
for col in range(30, 0, -1):
    ws.delete_cols(col)

# Save the changes to the excel file
wb.save('file2.xlsx')
