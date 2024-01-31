"""
Input: arr[1,1,2,2,2,3,3]

Output: arr[1,2,3,_,_,_,_]
"""

def remove_duplicate_brute(arr, n):
    """
        put all the element in set where set cannot be contain any duplicate element and add set element in arr
    """
    st = set()
    for i in range(n):
        st.add(arr[i])  # insertion in worst case contain O(N*logN) and sc is O(N) becouse if all are unique element 

    k = len(st)
    j = 0
    for i in st:  # O(N)
        arr[j] = i
        j += 1

    return k

def remove_duplicate_optimal(arr, n):
    """ 
    - initalize i = 0 
    - loop j in range between 1 to N
    - compare if arr[j] is not equal to arr[i] then incraent i and arr[i] become arr[j]
    - finally return i + 1
    """
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


arr = [1,1,2,2,2,3,3]
postion = remove_duplicate_brute(arr, len(arr))
for i in range(postion):
    print(arr[i], end=" ")

# overall TC: O(N*logN) + O(N) SC: O(N)
    
postion2 = remove_duplicate_optimal(arr, len(arr))
for i in range(postion2):
    print(arr[i], end=" ")

