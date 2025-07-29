l=1
r=7
for i in range(1,5):
    for j in range(1,8):
        if j>=l and j<=r:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    l+=1
    r-=1
