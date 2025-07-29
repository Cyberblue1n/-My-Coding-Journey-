#average temperature from list
def array_creation(n):
    arr = []
    for i in range(1, n+1):
        a = int(input(f"Day{i}'s high temp: "))
        arr.append(a)
    return arr
    
def average_temp(arr):
    avg_temp = sum(arr)/len(arr)
    return avg_temp

def high_temp_days(arr, avg_temp):
    avg = avg_temp
    for i in range(0, len(arr)):
        if arr[i] > avg:
            print(f"Day{i+1} is high temperature than average")

if __name__=="__main__":
    n = int(input("How many days's temperature: "))
    myarr = array_creation(n)
    val = average_temp(myarr)
    print("Average temperature is ",val)
    high_temp_days(myarr, val)