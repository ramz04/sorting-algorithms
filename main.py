def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    middle = len(nums) // 2

    left_half_nums = nums[:middle]
    right_half_nums = nums[middle:]

    left_half_nums = merge_sort(left_half_nums)
    right_half_nums = merge_sort(right_half_nums)

    return merge(left_half_nums, right_half_nums)


def merge(first: list[int], second: list[int]) -> list[int]:
    final = []
    i, j = 0, 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    final += first[i:]
    final += second[j:]

    return final
