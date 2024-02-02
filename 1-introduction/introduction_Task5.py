from typing import Tuple


l = 100000000


def get_sum_of_multiples(limit: int, m: int | Tuple[int, int]) -> int:
    """
    Calculate the sum of all multiples below the limit
    :param limit: int: Limit number (exclusive)
    :param m: int or Tuple of 2 ints - multiple(s)
    :return: int: sum of all multiples
    """
    if type(m) is int:
        return m * ((limit - 1) // m) * ((limit - 1) // m + 1) // 2
    else:
        return (get_sum_of_multiples(limit, m[0]) +
                get_sum_of_multiples(limit, m[1]) -
                get_sum_of_multiples(limit, m[0]*m[1]))


if __name__ == "__main__":
    print(get_sum_of_multiples(l, (3, 5)))
