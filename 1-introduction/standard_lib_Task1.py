import random


l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]


def filter_list(l):

    # •	“for” loop
    def for_filter_list():
        for i in l:
            if type(i) is not int:
                l.remove(i)
        return l

    # •	list comprehensions
    def list_compr():
        return [i for i in l if type(i) is int]

    # •	filter() + lambda
    def lambda_filter():
        return list(filter(lambda i: type(i) is int, l))

    functions = random.choice((for_filter_list, list_compr, lambda_filter))
    return functions()


filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

