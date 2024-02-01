"""
Example 1:
Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.

Example 2:
Input Format: N = 3, array[] = {1,3}
Result: 2
"""

def missing_number_in_array_brute(arr, n):
    for i in range(1, n+1):  #O(N)
        flag = 0

        for j in range(len(arr)):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
    return -1
        
def missing_number_in_array_optimal(arr, n):
    array_sum = sum(arr)
    n_sum = (n * (n + 1))//2
    return n_sum - array_sum


n = 5
arr = [1,2,3,4]
print(missing_number_in_array_brute(arr, n))
# Overall TC: O(N) SC: O(1)
print(missing_number_in_array_optimal(arr, n))

