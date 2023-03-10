import csv

with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/test/data_test.csv', 'r', encoding='utf-8') as file:
    dialect = csv.Sniffer().sniff(file.readline())
    print(dialect.delimiter)
