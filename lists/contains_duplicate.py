def contains_duplicate(numbers: list[int]) -> bool:
    seen_so_far = set()
    for number in numbers:
        if number not in seen_so_far:
            seen_so_far.add(number)
        elif number in seen_so_far:
            return True
    return False

assert contains_duplicate([1,2,3,1]) == True
assert contains_duplicate([1,2,3,4]) == False
assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True
