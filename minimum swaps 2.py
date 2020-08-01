def minimumSwaps(arr,n):
    i = 0
    swaps = 0
    while i < n:
        if arr[i] != i+1:
            k = arr[i]
            arr[i], arr[k-1] = arr[k-1], arr[i]
            swaps += 1
        else:
            i += 1
    return swaps
