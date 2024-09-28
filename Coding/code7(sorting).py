def bubble_sort(arr, n):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            '''
            for checking each iterartions
            print(arr)
            '''
    return arr

if __name__ == "__main__":
    arr = []
    n = int(input("Enter size of the array "))
    for i in range(n):
        ele = input("Enter array element: ")
        arr.append(ele)
    print("Array elements are: ",arr)
    a = bubble_sort(arr, n)
    print("Sorted array: ",a)



