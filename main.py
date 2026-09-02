def quick_sort(nums: list[int], low: int, high: int) -> None:
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)


def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1
    