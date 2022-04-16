def custom_filter(function, iterable):
    """
    :param function: A boolean function.
    :param iterable: An iterable to run on it the given function.
    :return: An iterable containing only the elements that the given function return true for each of them.
    """
    return [item for item in iterable if function(item)]


def is_even(num):
    """
    :param num: An integer to check if it even number.
    :return: True if the number is even else False.
    """
    return num % 2 == 0


if __name__ == '__main__':
    print(custom_filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
