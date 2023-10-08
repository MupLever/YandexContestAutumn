"""
Требуется удалить из массива все 0, не изменяя размера массива, 
поэтому конец массива надо заполнить нулями.
"""

def remove_zero(nums: list) -> None:
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], l = nums[r], l + 1

    for i in range(l, len(nums)):
        nums[i] = 0
