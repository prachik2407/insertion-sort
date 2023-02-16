def insertion_sort(arr):

    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
                
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            
        arr[j + 1] = x

arr = [9, 8, 61, 7, 1]
insertion_sort(arr)
print('Sorted Array: ', arr)