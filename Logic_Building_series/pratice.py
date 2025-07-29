
def check_even(num):
    n = str(num)
    for i in n:
        if int(i)%2!=0:
            return False
    return True

n = 2222220222

print(check_even(n))