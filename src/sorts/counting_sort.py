# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="rasmadeus"
__date__ ="$Mar 16, 2014 6:04:23 PM$"

def counting_sort(array, k):
    sorted = []
    equal_items_count = [0 for _ in range(k)]
    for item in array:
        equal_items_count[item] += 1
    for i in range(k):
        for _ in range(equal_items_count[i]):
            sorted.append(i)
    return sorted
