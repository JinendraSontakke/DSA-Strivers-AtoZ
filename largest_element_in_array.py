def largest_element_brute_force_approch(arr, n):
    """
        if we sort an array in accending order 
        and print the -1 index which is last index or 
        if we sort an array in decending order and print first index will be answer

        arr = [3,2,1,5,2]
        sorted arr in accending order [1,2,2,3,5]
        print last index   
    """
    arr.sort()  # here time complexity is O(n log n) and space also O(n)
    return arr[-1] # here time complxity is O(1) and space also o(1)

def largest_element_optimal_approch(arr,n):
    """
        If we consider the first element as the largest and traverse the array, comparing each element with the largest one.
    """

    largest = arr[0]        
    for i in range(1, n):           # TC: O(N)
        if arr[i] > largest:
            largest = arr[i]

    return largest

arr = [3,2,1,5,2]
print(largest_element_brute_force_approch(arr, len(arr)))

# overall brute force TC : O(nlogn)
# overall brute force SC: O(N)


print(largest_element_optimal_approch(arr, len(arr)))
# overall optimal TC: O(N)
# overall optimal SC: O(1)