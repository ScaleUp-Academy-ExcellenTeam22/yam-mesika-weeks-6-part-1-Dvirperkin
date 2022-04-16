def get_positive_numbers():
    """
    Functions that read numbers from the user and return a list of the positive entered numbers.
    :return: A list of the positive entered numbers.
    """
    user_numbers = [int(x) for x in input("Enter numbers separate by comma:\n").split(',')]
    return list(filter(lambda number: number > 0, user_numbers))


if __name__ == '__main__':
    print(get_positive_numbers())