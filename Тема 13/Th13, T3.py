def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

def choose_func(nums, func1, func2):
    nums_new = []
    for item in nums:
        if item >= 0:
            nums_new.append(item)
        else:
            pass
    if len(nums_new) == len(nums):
        print(square_nums(nums_new))
    else:
        print(remove_negatives(nums_new))
    

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

choose_func(nums1, square_nums, remove_negatives)
choose_func(nums2, square_nums, remove_negatives)
        
        
        
    

