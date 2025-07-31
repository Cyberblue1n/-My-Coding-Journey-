def push_zeros_to_end(arr):
    i = 0
    for num in range(len(arr)):
        if arr[num]!=0:
            arr[i], arr[num] = arr[num], arr[i]
            i+=1

    return arr
if __name__ == "__main__":
    arr = [1,2,0,4,3,0,5,0]
    print(push_zeros_to_end(arr))