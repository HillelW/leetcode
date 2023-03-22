def could_be_palindrome(string: str) -> bool:
    """constraints:
    1. if at most one character is changed, the string can be a palindrome.
    2. input string does not have any spaces and only consist of ASCII characters.

    time complexity: O(n), where n is the length of the input string.
    space complexity: O(1).
    """
    if not string:
        return False

    string_length: int = len(string)
    left_index: int = 0
    right_index: int = string_length - 1

    number_of_mismatches = 0
    while left_index < right_index:
        if string[left_index] != string[right_index]:
            number_of_mismatches += 1
        left_index += 1
        right_index -= 1
    if number_of_mismatches < 2:
        return True
    return False

assert could_be_palindrome('racecas') == True
assert could_be_palindrome('racecar') == True
assert could_be_palindrome('racecbs') == False