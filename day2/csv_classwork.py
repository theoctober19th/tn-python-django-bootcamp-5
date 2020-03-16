import csv

with open('email.csv') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        if row['Last name'][0].lower() == 'j':
            print(row['Login email'])