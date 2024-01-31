"""
Input: N = 5, array[] = {1,2,3,4,5}
Output: 2,3,4,5,1
"""
def left_rotate_array_brute(arr, n):
    """
        take temp array of size of n and store element from 2nd index and then at last put first element in temp.
    """
    if n < 2:
        return arr

    temp = [0] * n   # SC: O(N)
    for i in range(1, n):  # TC: O(N)
        temp[i-1] = arr[i]

    temp[n-1] =  arr[0]

    return temp

def left_rotate_array_optimal(arr, n):
    """
        run loop form 1 index to last and sift to left and asign temp to last index of array 
    """
    temp = arr[0]          # SC: O(1)
    for i in range(1, n):  # TC : O(N)
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

arr = [1,2,3,4,5]
print(left_rotate_array_brute(arr, len(arr)))

# overall TC: O(N) SC:O(N)

print(left_rotate_array_optimal(arr, len(arr)))

# overall TC: O(N) SC: O(1)

