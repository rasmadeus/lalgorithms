# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="rasmadeus"
__date__ ="$Mar 9, 2014 3:32:19 PM$"

def _copy(src, dst, dst_left):
    for item in src:
        dst[dst_left] = item
        dst_left += 1

def _merge(array, left, middle, right):
    temp_array = []
    i_one = left
    i_two = middle
    while True:
        if i_one == middle and i_two == right:
            break
        if i_one == middle and i_two != right:
            temp_array.append(array[i_two])
            i_two += 1
        if i_one != middle and i_two == right:
            temp_array.append(array[i_one])
            i_one += 1
        if i_one != middle and i_two != right:
            if array[i_one] > array[i_two]:
                temp_array.append(array[i_two])
                i_two += 1
            else:
                temp_array.append(array[i_one])
                i_one += 1
    _copy(temp_array, array, left)

def merge_sort(array):
    _merge_sort(array, 0, len(array))

def _merge_sort(array, begin, end):
    if end - begin <= 1:
        return
    if end - begin == 2:
        if array[end - 1] < array[begin]:
            array[begin], array[end - 1] = array[end - 1], array[begin]
            return
    middle = begin + int((end - begin) / 2)
    _merge_sort(array, begin, middle)
    _merge_sort(array, middle, end)
    _merge(array, begin, middle, end)
    