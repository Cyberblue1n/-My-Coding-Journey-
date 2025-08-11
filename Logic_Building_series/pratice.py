def maxProduct(arr):
    max_val = float('-inf')
    sum = 1
    for i in arr:
        sum*=i
        if sum>max_val:
            max_val = sum
        if sum<0:
            sum = 1
            
    return max_val


arr = [-2, 6, -3, -10, 0, 2]
print(maxProduct(arr))