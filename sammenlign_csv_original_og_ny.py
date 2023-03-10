import csv

def compare_csv_files(data_cleaned_original, data_cleaned):
    rows_in_data_cleaned_original = set()
    rows_in_data_cleaned = set()

    with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_cleaned_original.csv', "r", encoding="utf-8-sig", newline="") as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row:
                rows_in_data_cleaned_original.add(tuple(row))

    with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_cleaned.csv', "r", encoding="utf-8-sig", newline='') as f2:
        reader = csv.reader(f2)
        for row in reader:
            if row:
                rows_in_data_cleaned.add(tuple(row))
            
    not_present_in_data_cleaned_original = rows_in_data_cleaned - rows_in_data_cleaned_original
    
    return not_present_in_data_cleaned_original

not_present = compare_csv_files("data_cleaned_original.csv", "data_cleaned.csv")
if not_present:
    print("The following rows are not present in data_cleaned_original.csv:")
    with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/new_geometry.csv', "w", newline="") as f3:
        writer = csv.writer(f3)
        for row in not_present:
            # Strip leading and trailing double quotes from each field in the row
            stripped_row = [field.strip('"') for field in row]
            writer.writerow(stripped_row)
            print(row)
else:
    print("All rows in data_cleaned.csv are present in data_cleaned_original.csv.")

