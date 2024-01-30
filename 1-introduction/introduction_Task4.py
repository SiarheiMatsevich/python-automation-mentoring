from sys import maxsize


def file_size(size_in_bytes):
    def converter(value, unit='B'):
        units = ['B', 'Kb', 'Mb', 'Gb']
        value = round(float(value), 1)
        if value / 1024 < 1 or unit == units[-1]:
            return value, unit
        else:
            return converter(value / 1024, units[units.index(unit)+1])
    return ''.join(map(str, converter(size_in_bytes)))


assert file_size(19) == '19.0B'
assert file_size(12345) == '12.1Kb'
assert file_size(1101947) == '1.1Mb'
assert file_size(572090) == '558.7Kb'
assert file_size(999999999999) == '931.3Gb'
print(f'The sys.maxsize is = {file_size(maxsize)}')
