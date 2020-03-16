import csv

with open('out.csv', 'w') as file:
    fieldnames = ['sn', 'name', 'email']
    writer = csv.DictWriter(file, fieldnames)
    writer.writeheader()
    dicts = [{
        'sno': 1,
        'name': 'Bikalpa',
        'email': 'abc@xyz.com'
    }, {
        'sn': 2,
        'name': 'Bikasdfalpa',
        'email': 'abc@dfxyz.com'
    }]
    try:
        writer.writerows(dicts)
    except ValueError:
        print('check input again')
    finally:
        print('i execute anyhow')