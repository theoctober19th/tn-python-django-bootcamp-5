import csv

with open('data.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['sex'] == 'F':
            print(row['name'])