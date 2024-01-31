"""
Example 1:
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
"""
def move_all_zero_end_brute_force(arr, n):
    """
        - create temp array
        - add non zero element in temp
        - add temp element in array 
        - put remmening as zero.
    """
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    for i in range(len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp),n):
        arr[i] = 0

    return arr

def move_all_zero_end_optimal(arr, n):
    """
        - first find index where first 0 occurace and assign to j if not then return array
        - from j + 1 index start serching non zero element and swap i and j and increment j by 1
    """
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    if j == -1:
        return arr
    
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

arr = [1,0,2,3,0,4,0,1]
print(move_all_zero_end_brute_force(arr, len(arr)))
# overall O(2*N) SC O(N)
print(move_all_zero_end_optimal(arr, len(arr)))
# overall O(N) SC(1)
