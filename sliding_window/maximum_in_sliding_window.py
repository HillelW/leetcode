def maximum_in_sliding_window(numbers: list[int], window_size: int) -> list[int]:
    window_maximums: list[int] = []
    list_lenth: int = len(numbers)

    if not numbers:
        return []
    
    left: int = 0
    right: int = left + window_size

    while right < list_lenth + 1:
        current_list: list[int] = numbers[left: right]
        max_int: int = max(current_list)
        window_maximums.append(max_int)

        left += 1
        right += 1
        
    return window_maximums

assert maximum_in_sliding_window([-4, 2, -5, 3, 6], 3) == [2, 3, 6]
assert maximum_in_sliding_window([], 3) == []
