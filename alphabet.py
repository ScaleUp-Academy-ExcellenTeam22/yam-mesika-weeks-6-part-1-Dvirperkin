def get_letters():
    """
    :return: A list containing all the capital and the lower alphabet.
    """
    return [chr(char_unicode) for char_unicode in range(ord("A"), ord("z") + 1)
            if char_unicode not in range(ord("Z"), ord("a"))]


if __name__ == '__main__':
    print(get_letters())
