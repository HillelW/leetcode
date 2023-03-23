def roman_numeral_string_to_integer(roman_numeral: str) -> int:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = len(roman_numeral)
    result = roman_map[roman_numeral[n - 1]]

    for i in range(n - 2, -1, -1):
        current_number = roman_map[roman_numeral[i]]
        previous_number = roman_map[roman_numeral[i + 1]]

        if roman_map[roman_numeral[i]] >= previous_number:
            result += current_number
        else:
            result -= current_number
    return result


assert roman_numeral_string_to_integer("XIV") == 14
