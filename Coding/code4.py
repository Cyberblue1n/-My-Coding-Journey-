#Python Program to Check Prime Number
def prime(n):
    for i in range (2,int(n/2)+1):
        if(n%i==0):
            return 0
        else:
            return 1
    return 1
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    a = prime(n)
    if a==1:
        print(f"{n} is the prime number")
    else:
        print(f"{n} is the non prime number")

