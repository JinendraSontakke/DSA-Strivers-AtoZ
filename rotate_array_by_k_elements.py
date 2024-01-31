"""
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
"""

def rotate_array_by_k_brute(arr, n, k):
    """
        - took temp and store the k indexs element in temp
        - shift the remaining index in left side 
        - put back temp at end of array
    """
    temp = []  # SC: O(K)
    for i in range(k):   # TC: O(k)
        temp.append(arr[i])

    for i in range(k, n):   # TC: O(N)
        arr[i - k] = arr[i]

   
    for j in range(n-k, n): 
        arr[i] = temp[j-(n- k)]
        
    
    return arr

def rotate_array_by_k_optimal(arr, n, k):
    """
        - fist reverse 0 to k
        - reverse k - n
        - reverse complete array
    """
    def reverse(arr, start, end):
        while start < end: #TC : O(N)
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)

    return arr

arr = [1,2,3,4,5,6,7]
k  = 2
print(rotate_array_by_k_brute(arr, len(arr), k))
# overall TC: O(N) SC: O(K)

print(rotate_array_by_k_optimal(arr, len(arr), k))
# overall TC: O(N) SC: O(1)
