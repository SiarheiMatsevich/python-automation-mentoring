from typing import Any


# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries


def merge_elems(*elems: Any) -> Any:
    """
    Recursively merges iterable items into flattened sequence
    :rtype: the next single element from given sequence that not iterable itself
    :param elems: elements to be merged
    """
    for elem in elems:
        if hasattr(elem, '__iter__') and (hasattr(elem, '__next__') or len(elem) != 1):
            yield from merge_elems(*elem)
        elif hasattr(elem, '__iter__') and (len(elem) == 1):
            yield elem[0]
        else:
            yield elem


# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')

# output: 1 2 3 6 z h a b a 1 2 3 4

# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception


def map_like(fun, *elems: Any) -> Any:
    """
    Apply given function to each element from *elems param. If the function cannot be applied yields an element as is +
    exception text in the following format:
    "element: exception text"
    :param fun: Function to be applied
    :param elems: Elements to apply function on
    """
    for i in elems:
        try:
            yield fun(i)
        except Exception as e:
            yield f'{i}: {e}'


# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]

for _ in map_like(fun, a, b, c, d):
    print(_)

# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable
