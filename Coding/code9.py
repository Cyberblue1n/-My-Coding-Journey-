def selection_Sort(arr):
    n = len(arr)
    for i in range (n):
        min = i
        for j in range(i+1, n):
            if(arr[min]>arr[j]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr
if __name__ =="__main__":
    arr = [4, 8, 5, 2, 1]
    print("Actual list: ",arr)
    a = selection_Sort(arr)
    print("Sorted list ",a)
