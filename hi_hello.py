def words_length(sentence: str) -> list:
    """
    A function that gets a string and returns a list that contains the length of each word.
    :param sentence: A string to measure.
    :return: A list that contains the length of each word.
    """
    return [len(word) for word in sentence.split()]


if __name__ == '__main__':
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
