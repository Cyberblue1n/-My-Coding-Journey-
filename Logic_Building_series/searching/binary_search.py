def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high = mid-1
        elif arr[mid]<target:
            low = mid +1
    
    return -1
        
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    target = 11
    if binary_search(arr, target)!= -1:
        print(f"{target} is found at index {binary_search(arr, target)}")
    else:
        print(f"{target} is not found")