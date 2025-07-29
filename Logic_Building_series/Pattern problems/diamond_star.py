n=7
l=4
r=4
for i in range(1,n+1):
    for j in range(1, n+1):
        if(j>=l and j<=r):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
    if i<=n//2:
        l-=1
        r+=1
    else:
        l+=1
        r-=1
         