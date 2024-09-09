def issymetric(s):
    i = 0
    j = len(s)//2
    while i<(len(s)//2):
        if s[i]==s[j]:
            i+=1
            j+=1
        else:
            return 0
    return 1

if __name__ == "__main__":
    s = input("Enter a word: ")
    a = issymetric(s)
    if a==1:
        print(f"{s} is symmetric word")
    else:
        print(f"{s} is not symmetric word")