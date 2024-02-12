import csv
data=[
['Name','Age','City']
['Max',30,'Munich']
['Betty',20,'Berlin']
['Uta',35,'Frankfurt']
['Sam',25,'Dresden']
]
def filters_csv(csv_file_path):
    with  open (csv_file_path,'r', newline=' ') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            if row(['Name']).startwith('A'):
                print(row)
csv_file_path='data.csv'
filters_csv(csv_file_path)