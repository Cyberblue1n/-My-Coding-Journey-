#Determine if a number is a palindrome.
def palindrome(n):
    i = 0
    j = len(n)-1
    while(i<j):
        if(n[i]==n[j]):
            i+=1
            j-=1
        else:
            return f"{n} is Not palindrome"
    return f"{n} is palindrome"

n=input("Enter number to check palindrome or not: ")
a = palindrome(n)
print(a)

