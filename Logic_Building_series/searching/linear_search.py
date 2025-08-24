def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i+1
    return False
if __name__ == "__main__":
    arr = [3,2,1,5,8,7,10,21,12,18,6]
    target = 19
    if linear_search(arr, target):
        print(f"{target} is found at index {linear_search(arr, target)}")
    else:
        print(f"{target} is not found")