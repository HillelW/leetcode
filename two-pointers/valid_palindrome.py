def is_palindrome(string: str) -> bool:
    """constraints:
    1. 1 <= len(string) <= 10^5.
    2. input string does not have any spaces and only consist of ASCII characters.

    time complexity: O(n), where n is the length of the input string.
    space complexity: O(1).
    """
    if not string:
        return False

    string_length: int = len(string)
    left_index: int = 0
    right_index: int = string_length - 1

    while left_index < right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


assert is_palindrome("abcba") == True
assert is_palindrome("hello") == False
assert is_palindrome() == False
assert is_palindrome("") == True
