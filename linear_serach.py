"""
Example 1:
Input: arr[]= 1 2 3 4 5, num = 3
Output: 2
"""

def linear_serach(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i
        
    return -1

arr = [1,2,3,4,5]
num = 3
print(linear_serach(arr, len(arr), num))
# overall TC: O(N) SC O(1)
