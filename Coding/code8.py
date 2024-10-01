def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j]>key:    #for decending order use arr[j]<key
            arr[j+1]=arr[j]
            j = j - 1
            arr[j+1]=key
    return arr

if __name__ =="__main__":
    arr = [4,8,1,2]
    print("Actual array: ",arr)
    a = insertion_sort(arr)
    print("Sorted array: ",a)
