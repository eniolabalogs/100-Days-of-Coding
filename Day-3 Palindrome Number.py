def Palindrome_Number(x):
    if x<0:
        return False
    else:
        if str(x)==(str(x)[::-1]):
            return True
        else:
            return False
print(Palindrome_Number(121))
print(Palindrome_Number(211))
print(Palindrome_Number(202))