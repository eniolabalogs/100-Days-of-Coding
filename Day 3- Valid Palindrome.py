def isPalindrome(s):
    a=""
    for i in s:
        if i.isalnum():
            a=a+i
    a=a.lower()
    return a==a[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
