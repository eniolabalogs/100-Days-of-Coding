def isValid(s):
    """
    count=0
    for i in range(len(s)):
        if s[i] =="(":
            count+=1
        if s[i] == "{":
            count+=2
        if s[i] == "[":
            count+=3
        if s[i] == ")" and s[i-1]=="(":
            count=count-1
        if s[i] == "}" and s[i-1]=="{":
            count= count-2
        if s[i]== "]" and s[i-1]== "[":
            count=count-3
    if count == 0:
        return True
    if count != 0:
        return False
    """
    stack = []
    diction = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in diction:
            a = stack.pop() if stack else '#'
            if diction[i] != a:
                print(a)
                return False
        else:
            stack.append(i)
    print (a)
    return not stack



print(isValid("]())"))