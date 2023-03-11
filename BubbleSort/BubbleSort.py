def bubble_sort(to_sort, lower_first=True):
    for i in range(len(to_sort)):
        for j in range(len(to_sort) - 1):
            if lower_first:
                sort_condition = to_sort[j] > to_sort[j + 1]
            else:
                sort_condition = to_sort[j] < to_sort[j + 1]
            if sort_condition:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]


arr = [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11]
bubble_sort(arr)
print(arr)
bubble_sort(arr, lower_first=False)
print(arr)
