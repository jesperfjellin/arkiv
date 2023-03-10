import csv

def compare_csv_files(file1, file2):
    rows_in_file1 = set()
    rows_in_file2 = set()

    with open(file1, "r", encoding="utf-8-sig") as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row:
                rows_in_file1.add(tuple(row))
            
    with open(file2, "r", encoding="utf-8-sig") as f2:
        reader = csv.reader(f2)
        for row in reader:
            if row:
                rows_in_file2.add(tuple(row))
            
    not_present_in_file1 = rows_in_file2 - rows_in_file1
    
    return not_present_in_file1

not_present = compare_csv_files("file1.csv", "file2.csv")
if not_present:
    print("The following rows are not present in file1.csv:")
    with open("file3.csv", "w") as f3:
        writer = csv.writer(f3)
        for row in not_present:
            writer.writerow(row)
            print(row)
else:
    print("All rows in file2.csv are present in file1.csv.")
