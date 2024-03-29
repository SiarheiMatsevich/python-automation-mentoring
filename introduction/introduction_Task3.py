import string


input_str = '''Python is an interpreted high-level programming language for general-purpose programming. Created by 
Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, 
notably using significant whitespace. It provides constructs that enable clear programming on both small and large 
scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years. 
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, 
including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library. 
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, 
is open source software and has a community-based development model, as do nearly all of Python's other 
implementations. Python and CPython are managed by the non-profit Python Software Foundation.'''


def get_most_used_letter_and_word_count(text: str, word: str) -> None:
    """
    Prints most used letter in text ignoring case and print how many times particular word is used in provided text.
    :param text: Given string where evaluation will be performed
    :param word: Given world which will be count in the text (ignoring case)
    """
    normalized_str = text.lower()
    count = [normalized_str.count(i) for i in string.ascii_lowercase]
    top_used = string.ascii_lowercase[count.index(max(count))]
    word_count = normalized_str.count(word.lower())
    return f'Letter "{top_used}" is used most often\nThe word "Python" is used {word_count} times.'



if __name__ == "__main__":
    print(get_most_used_letter_and_word_count(input_str, 'Python'))
