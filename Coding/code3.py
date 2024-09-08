#Python Program to Check if a Number is Odd or Even

def odd_even(n):
    if(n%2==0):
        return 1
    else:
        return 0
#driver code
if __name__ == "__main__":
    print("Enter a number: ")
    n = int(input())
    a = odd_even(n)
    if a==1:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")

