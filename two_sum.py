"""
 N = 5, arr[] = {2,6,5,8,11}, target = 14
"""

def two_sum_brute(arr, n, target):
    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j]:
                continue
            if arr[i] + arr[j] == target:
                return [i, j]
            
    return -1

def two_sum_optimal(arr, target):
    dic = {}
    for i, num in enumerate(arr):
        cop = target - num

        if cop in dic:
            return [dic[cop], i]
        dic[num] = i

    return -1

arr= [2,6,5,8,11]
n = 5
target = 14
print(two_sum_brute(arr, n, target))
# overall TC: O(N^2) SC = O(1)
print(two_sum_optimal(arr, target))
# overall TC: O(N) SC(N)

