"""
Example 1:
Input: [1,2,4,7,7,5]
Output: Second Largest : 5
"""

def second_largest_brute_force(arr, n):
    "if we sort an array in accendign order and write -2 or verifty that it not equl to largest"
    if n < 2:
        return -1
    
    arr.sort() # tc: O(NlogN) SC: O(N)
    largest = arr[-1]
    second = float('-inf')
    for i in range(n-1, -1, -1):  # TC: O(N)
        if arr[i] != largest:
            second = arr[i]
            break
    return second

def second_largest_better(arr, n):
    """
        first find largest using tarversing an array 
        then using another loop traversing and comparign largest find second largest
    """
    if n < 2:
        return -1
    
    largest = arr[0]
    for i in range(1, n):  # ~O(N)
        if arr[i] > largest:
            largest = arr[i]

    second_largest = float('-inf')
    for i in range(n):  # O(N)
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest

def second_largest_optimal(arr, n):
    if n < 2:
        return -1
    
    largest = arr[0]
    second_largest = float('-inf')

    for i in range(1, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest

arr = [1,2,4,7,7,5]
n = len(arr)
print(second_largest_brute_force(arr, n))
#overall tc: O(NlogN) SC: O(N)

print(second_largest_better(arr, n))
#overall TC: O(N) SC: O(1)

print(second_largest_optimal(arr, n))
#overall TC: ~ O(N) SC: O(1)

