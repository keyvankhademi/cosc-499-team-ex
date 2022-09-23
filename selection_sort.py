def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        minVal = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = minVal
    return arr
        