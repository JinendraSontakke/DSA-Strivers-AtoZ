def issorted_brute_force(arr, n):
    """
        using two pointer method will compare next element is greater or not 
    """
    for i in range(n):  #O(N)
        for j in range(i, n):  #O(N)
            if arr[i] > arr[j]:
                return False
    return True  # O(N*N) = O(N^2)

def issorted_optimal(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i -1]:
            return False
        
    return True

arr1 = [1,2,3,4,5]
arr2 = [5,4,6,7,8]

print(issorted_brute_force(arr1, len(arr1)))
print(issorted_brute_force(arr2, len(arr2)))

# Overall TC: O(N^2) SC: O(1)

print(issorted_optimal(arr1, len(arr1)))
print(issorted_optimal(arr2, len(arr2)))

# Overall TC: O(N) SC: O(1)