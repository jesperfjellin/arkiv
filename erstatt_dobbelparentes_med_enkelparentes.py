import csv

with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_json.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = []
    for row in reader:
        rows.append([cell.replace('((','(').replace('))',')') if isinstance(cell, str) else cell for cell in row])

with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_json.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
