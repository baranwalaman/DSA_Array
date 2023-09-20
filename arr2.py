def linearSearch(arr, x):
    for i in range(0, len(arr)):
        if(arr[i] == x):
            return i
    return -1


arr = [2, 34, 56, 51, 88, 26, 39]
x = 88
result = linearSearch(arr, x)
print("The index of the element is", result)