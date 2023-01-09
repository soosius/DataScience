def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort):
    if (
        len(list_to_sort) > 1
        and not len(list_to_sort) < 1
        and len(list_to_sort) != 0
    ):
        mid = len(list_to_sort) // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
plt.yticks(ticks=[20,40,60,80])
plt.xticks(ticks=[])
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
