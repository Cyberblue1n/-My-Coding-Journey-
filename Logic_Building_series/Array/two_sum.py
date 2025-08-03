'''
Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

Examples:

Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: true
Explanation: arr[3] + arr[4] = -3 + 1 = -2
Input: arr[] = [1, -2, 1, 0, 5], target = 0
Output: false
Explanation: None of the pair makes a sum of 0
Input: arr[] = [11], target = 11
Output: false
Explanation: No pair is possible as only one element is present in arr[]
Constraints:

1 ≤ arr.size ≤ 10^5
-105 ≤ arr[i] ≤ 10^5
-2*105 ≤ target ≤ 2*10^5
'''

def two_sum(arr, target):
    my_map = {}
    for index, num in enumerate(arr):
        value = target - num
        if value in my_map:
            return True
        my_map[num] = index
        
    return False

if __name__ == "__main__":
    arr = [0,-1,2,-3,1]
    target = -2
    print(two_sum(arr, target))