def sum_of_three_values_brute_force(nums: list[int], target: int) -> bool:
    """time complexity: O(n^3), where n is the length of the input string.
    space complexity: O(1)."""
    if not nums or not target:
        return False

    list_length: int = len(nums)
    for i in range(list_length - 2):
        for j in range(i + 1, list_length - 1):
            for k in range(j + 1, list_length):
                sum_of_three_values = nums[i] + nums[j] + nums[k]
                if sum_of_three_values == target:
                    return True
    return False


assert sum_of_three_values_brute_force([1, 2, 3], 6) == True
assert sum_of_three_values_brute_force([1, 4, 45, 6, 10, 8], 22) == True
assert sum_of_three_values_brute_force([1, 2, 3], 5) == False
assert sum_of_three_values_brute_force([], 5) == False
assert sum_of_three_values_brute_force([1, 2, 3], None) == False


def sum_of_three_values(nums: list[int], target: int) -> bool:
    """time complexity: O(n^2), where n is the length of the input string.
        space complexity: O(1).

        Sort the given array.
    Loop over the array and fix the first element of the possible triplet, arr[i].
    Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum,
    If the sum is smaller than the required sum, increment the first pointer.
    Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
    Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break.
    """
    if not nums or not target:
        return False

    nums.sort()

    list_length = len(nums)
    for i in range(list_length - 2):
        left = i + 1
        right = list_length - 1

        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]

            if total_sum == target:
                return True

            if total_sum < target:
                left += 1

            elif total_sum > target:
                right -= 1
    return False


assert sum_of_three_values([1, 2, 3], 6) == True
assert sum_of_three_values([1, 4, 45, 6, 10, 8], 22) == True
assert sum_of_three_values([1, 2, 3], 5) == False
assert sum_of_three_values([], 5) == False
assert sum_of_three_values([1, 2, 3], None) == False
