n = int(input("Enter a number: "))
l=1
r=7
for i in range (1, n+1):
    for j in range(1, n+1):
        if j==l or j==r:
            print("*", end="")
        else:
            print(" ",end="")
    print()
    l+=1
    r-=1
