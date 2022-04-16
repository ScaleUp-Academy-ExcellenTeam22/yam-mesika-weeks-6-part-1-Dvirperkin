def full_names(first_names, last_names, min_length=-1):
    """
    :param first_names: A list of first names.
    :param last_names: A list of last names.
    :param min_length: A minimum length of full name to return.
    :return: A list containing all possible threads between first names to last names.
    """
    first_last_names = [(first + " " + last).title() for first in first_names for last in last_names]
    if min_length > -1:
        first_last_names = list(filter(lambda name: len(name) > min_length, first_last_names))
    return first_last_names


if __name__ == '__main__':
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names))
    print(full_names(first_names, last_names, 10))
