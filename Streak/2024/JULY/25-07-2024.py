from random import randint


def partition(array: list[int], low: int, high: int) -> int:
    # this is function for choosing pivot and partitate the array
    pivot: int = array[randint(low, high)]
    write_ind_smaller: int = low  # where to write elements smaller than pivot
    write_ind_greater: int = high  # where to write elements greater than pivot
    cur = low

    while cur < write_ind_greater + 1:
        num = array[cur]
        if num < pivot:
            array[write_ind_smaller], array[cur] = array[cur], array[write_ind_smaller]
            write_ind_smaller += 1
            cur += 1
        elif num > pivot:
            array[write_ind_greater], array[cur] = array[cur], array[write_ind_greater]
            write_ind_greater -= 1
        else:
            cur += 1

    return write_ind_smaller  # return index of the pivot


def quick_sort(array, low, high) -> None:  # [low, high]
    # Base case: if range is empty or contains only 1 element
    if low >= high:
        return

    pivot_ind: int = partition(array, low, high)
    quick_sort(array, low, pivot_ind - 1)  # left part
    quick_sort(array, pivot_ind + 1, high)  # right part


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quick_sort(nums, 0, len(nums) - 1)
        return nums
