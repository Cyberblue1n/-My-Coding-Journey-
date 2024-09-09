'''Python program to check whether the string is Palindrome
Input: khokho
Output: 
The entered string is not palindrome

Input:amaama
Output:
The entered string is palindrome'''

def ispalindrome(s):
    if s==s[::-1]:
        return 1
if __name__ == "__main__":
    s = input("Enter word: ")
    a = ispalindrome(s)
    if a==1:
        print(f"{s} is palindrome")
    else:
        print(f"{s} is not palindrome")
