"""
Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.

Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
"""

def more_than_one_brute(arr):
    for i in range(len(arr)):
        num = arr[i]
        count = 0
        for j in range(len(arr)):
            if arr[j] == num:
                count += 1
        
        if count == 1:
            return arr[i]
    return -1

def more_than_one_better(arr):
    dic = {}

    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    
    for i, val in dic.items():
        if val == 1:
            return i
    return -1
def more_than_one_optimal(arr):
    result = 0
    for i in arr:
        result ^= i

    return result

arr = [4,1,2,1,2]
print(more_than_one_brute(arr))
# overall TC: O(N^2) and SC: O(1)
print(more_than_one_better(arr))
# overall TC: O(N) and SC: O(N)
print(more_than_one_optimal(arr))
# overall TC: O(N) and SC: O(1)