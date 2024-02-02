import random
from typing import List

l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]


def filter_list(li: List) -> List:
    """
    Filters list of any items and return a list of integers from given list
    :param li: A list to be filtered
    :return:  list of integers from initial list
    """
    # •	“for” loop
    def for_filter_list():
        out = []
        for i in li:
            if type(i) is int:
                out.append(i)
        return out

    # •	list comprehensions
    def list_compr():
        return [i for i in li if type(i) is int]

    # •	filter() + lambda
    def lambda_filter():
        return list(filter(lambda i: type(i) is int, li))

    functions = random.choice((for_filter_list, list_compr, lambda_filter))
    return functions()


if __name__ == '__main__':
    assert filter_list([1, 2, 'a', 'b']) == [1, 2]
    assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]
    assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]
    assert filter_list(l) == [1, 2, 4, 10, 33]

