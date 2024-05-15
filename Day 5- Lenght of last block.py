def lengthOfLastWord(s):
    """
    s=s[::-1]
    c=0
    for i in s:
        if i.isalpha():
            c=c+1
        else:
            break
    return c
    """
    s=s.split()
    s=len(s[-1])
    return s

print(lengthOfLastWord("I am the real zar man"))