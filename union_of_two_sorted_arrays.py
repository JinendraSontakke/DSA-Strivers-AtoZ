"""
n = 5,m = 5.
arr1[] = {1,2,3,4,5}  
arr2[] = {2,3,4,4,5}
output: {1,2,3,4,5}

example 2 

n = 10,m = 7.
arr1[] = {1,2,3,4,5,6,7,8,9,10}
arr2[] = {2,3,4,4,5,11,12}
output: {1,2,3,4,5,6,7,8,9,10,11,12}
"""

def union_of_array_brute(arr1, arr2):
    """
        - initalize an empty set
        - initalize an empty union list
        - insert arr1 element in set
        - insert arr2 element in set
        - insert set element in union list
        - return union list
    """
    st = set()      # SC: O(M + N)
    union = []      # SC: O(N)

    for i in range(len(arr1)):
        st.add(arr1[i])  # TC: O(nlogn) 
    
    for i in range(len(arr2)): # TC: O(Mlogn)
        st.add(arr2[i])

    for i in st:
        union.append(i)

    return union

def union_of_array_optimal(arr1, arr2):
    """
        - initalize i and j as zero and union list as  empty 
        - check if len of arr1 and arr2 are less than i , j
        - if yes check if arr1[i] <= arr2[j] if yes then check union length == 0 or last elemetn of union not equal to arry 1 or 2
        - append and increment i  and j 
        - and add remaining element also using i and j 
    """
    i,j = 0, 0
    union = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])

        j += 1

    return union


            

arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
print(union_of_array_brute(arr1, arr2))
# overall TC: O(m+n * log m+n) SC: O(m+n)

print(union_of_array_optimal(arr1, arr2))
# overall TC: O(m+n) SC: O(1)



    

