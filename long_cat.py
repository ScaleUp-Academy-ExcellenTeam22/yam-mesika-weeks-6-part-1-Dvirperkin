def count_words(text):
    """
    :param text: An iterable text.
    :return: A dictionary of the length of each word in the given text - Example: "You: 3".
    """
    return {word: len(word) for word in text}


if __name__ == '__main__':
    my_text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    print(count_words(word.strip("?,!.()/\"") for word in my_text.split()))
