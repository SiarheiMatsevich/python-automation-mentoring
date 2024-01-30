from csv import DictReader
from json import dump


with open('cars.csv') as f:
    reader = DictReader(f)
    csv_dict = [row for row in reader]
    with open('cars.json', 'w') as j:
        dump(csv_dict, j, indent=2)
