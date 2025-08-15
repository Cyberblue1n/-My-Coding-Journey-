#Sort 0s, 1s and 2s
'''
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Note: You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?
Constraints:
1 ≤ arr.size() ≤ 10^6
0 ≤ arr[i] ≤ 2
'''
def partition(left, right, arr):
    p = arr[left]
    i = left+1
    j = right
    while True:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<=j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    
    arr[left], arr[j] = arr[j], arr[left]

    return j


def quicksort(left, right, arr):
    if left<=right:
       pivot = partition(left, right, arr) 
       quicksort(left, pivot-1, arr)
       quicksort(pivot+1, right, arr)
    
    return arr

if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2]
    i = 0
    j = len(arr)-1
    print(quicksort(i, j, arr))


 