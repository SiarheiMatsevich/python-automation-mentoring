from typing import List

numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]


def get_min_max(li: List) -> None:
    """
    Converts all convertible values from the list to integer using int() built-in function and prints max and min values
    :param li: list of items to be converted to int and find max and min values from
    """
    if li:
        out = list(filter(lambda i: hasattr(i, '__int__'), li))
        if len(out):
            print(f'Maximum value is: {max(out)}')
            print(f'Minimum value is: {min(out)}')
        else:
            print('No values can be converted to int in provided list')
    else:
        raise ValueError('List cannot be empty')


if __name__ == "__main__":
    get_min_max(numbers)
