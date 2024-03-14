from typing import List


def fizz_buzz() -> List:
    """
    Prints numbers from 1 to 100.
    If the number is a multiple of 3, the program displays the word Fizz instead.
    If the number is a multiple of 5, the word Buzz. 
    If the number is a multiple of both 3 and 5, then the program prints the word FizzBuzz.
    """
    res = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            res.append('FizzBuzz')
        elif i % 3 == 0:
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(i)

    return res


if __name__ == "__main__":
    print(*fizz_buzz())
