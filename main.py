def bubble_sort(nums: list[int]) -> list[int]:
    swap = True
    end = len(nums)

    while swap == True:
        swap = False
        
        for i in range(end - 1):
            i = i + 1
            if nums[i -1] > nums[i]:
                x = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = x
                swap = True
        end -= 1

    return nums
                
