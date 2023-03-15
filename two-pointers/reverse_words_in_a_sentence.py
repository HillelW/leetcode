def reverse_words_in_a_sentence(sentence: str) -> str:
    """constraints:
    1. The length of the input string should be equal to
    or more than one character or word.
    2. Sentence contains English uppercase and lowercase letters, digits, and spaces.
    3. The order of the letters within a word is not to be reversed.

    time complexity: O(n)
    space complexity O(n):
    """
    result = []
    words: list[str] = sentence.split(" ")
    for word in words[::-1]:
        result.append(word)
    return " ".join(result)


assert reverse_words_in_a_sentence("hello there again") == "again there hello"
