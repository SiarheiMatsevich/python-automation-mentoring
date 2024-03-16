from csv import DictReader
from json import dump
import re


def convert_csv_to_json(file_name: str) -> None:
    """
    Generates json file from given csv file
    :param file_name: csv file to be converted
    """
    with open(file_name) as f:
        reader = DictReader(f)
        csv_dict = list(reader)
        with open(re.sub(r'\.csv$', '.json', file_name), 'w') as j:
            dump(csv_dict, j, indent=2)


if __name__ == '__main__':
    convert_csv_to_json('cars.csv')
