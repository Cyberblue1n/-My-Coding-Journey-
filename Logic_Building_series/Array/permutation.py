def permutation(arr1, arr2):
    if len(arr1)!=len(arr2):
        return False
    
    arr1.sort()
    arr2.sort()

    if arr1==arr2:
        return True
    else:
        return False
    

arr1 = [1,2,3,4]
arr2 = [4,2,1,3]
print(permutation(arr1, arr2))