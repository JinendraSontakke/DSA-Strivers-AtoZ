def sort_zero_one_two_brute(arr):
    arr.sort()
    return arr

def sort_zero_one_two_better(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            count_0 +=1
        elif arr[i] == 1:
            count_1 += 1
        else:
            count_2 += 1
    
    for i in range(count_0):
        arr[i] = 0
    for i in range(count_0, count_0+count_1):
        arr[i] = 1
    for i in range(count_1+count_0, len(arr)):
        arr[i] = 2

    return arr

def sort_zero_one_two_optimal(arr):
    """
        Dutch Flag Algorithm
        - if arr[mid] == 0: swap low and mid and increament low and mid
        - if arr[mid] == 1: incramenet mid
        - if arr[mid] == 2: swap mid and high and decrement mid and high
    """

    mid, low = 0, 0
    high = len(arr)-1

    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

arr = [2,0,2,1,1,0]

print(sort_zero_one_two_brute(arr))
# #overall TC: O(nlogN) and SC(N)

print(sort_zero_one_two_better(arr))
# Overall TC: O(N) and SC O(1)
print(sort_zero_one_two_optimal(arr))
# # Overall TC: O(N) and SC O(1)