from typing import List

numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]


def get_min_max(li: List) -> str:
    """
    Converts all convertible values from the list to integer using int() built-in function and prints max and min values
    :param li: list of items to be converted to int and find max and min values from
    """
    if li:
        out = list(map(int, filter(lambda i: hasattr(i, '__int__'), li)))
        if len(out):
            return f'Maximum value is: {max(out)}\nMinimum value is: {min(out)}'
        else:
            return 'No values can be converted to int in provided list'
    else:
        raise ValueError('List cannot be empty')


if __name__ == "__main__":
    print(get_min_max(numbers))
