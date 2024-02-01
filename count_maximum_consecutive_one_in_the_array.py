def max_count(arr):
    max_count = 0
    coutn = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            coutn = 0
        else:
            coutn += 1
            max_count = max(max_count, coutn)

    return max_count

arr = [1, 0, 1, 1, 0, 1]
print(max_count(arr))