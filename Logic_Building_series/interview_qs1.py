'''
Ask By Company -: zoho , rockstand

Q1. Given two arrays a[] and b[],the task is to find the number of elements 
in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct
elements from both arrays. If there are repetitions, then only one element
occurrence should be there in the union.

Note:Elements are not necessarily distinct.

Examples:
Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3]
Output: 5
Explanation: 1, 2, 3, 4 and 5 are the elements which comes in the union setof both arrays. So
count is 5.

Input: a[] = [85, 25, 1, 32, 54, 6], b[] = [85, 2]
Output: 7
Explanation: 85, 25, 1, 32, 54, 6, and 2 are the elements which comes in the union set of both
arrays. So count is 7.

Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1]
Output: 2
Explanation: We need to consider only distinct. So count is 2.
Constraints:
1 ≤ a.size, b.size ≤ 10^5
0 ≤ a[i], b[i] < 10^5

'''

def union(arr1, arr2):
    unique = {}
    for x in arr1:
        unique[x] = True
    for x in arr2:
        unique[x] = True
    return len(unique)


if __name__ == "__main__":
    arr1 = [85, 25, 1, 32, 54, 6]
    arr2 = [85, 2]
    print(union(arr1, arr2))
