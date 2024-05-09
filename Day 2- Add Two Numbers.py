def addTwoNumbers(l1,l2):
    """
    s=[]
    a=([l1.pop()]+ l1)
    b=([l2.pop()]+ l2)
    a=[str(i) for i in a]
    b=[str(j) for j in b]
    a= "".join(a)
    b= "".join(b)
    c= int(a)+int(b)
    for i in range(len(str(c))):
        s.append(str(c)[i])
    s=s[::-1]
    s=[int(k) for k in s]
    print (s)
addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
addTwoNumbers([2,4,3],[5,6,4])
"""
    z=[]
    rem=0
    small_length=min(len(l1),len(l2))
    for i in range(small_length):
        a=l1[i]+l2[i]+ rem
        rem= a//10
        a=a%10
        z.append(a)
    if (len(l1))> small_length:
        for i in range ((len(l1))-small_length):
            a=l1[i]+rem
            rem=a//10
            a=a%10
            z.append(a)
    if (len(l2))>small_length:
        for i in range((len(l2))-small_length):
            a=l2[i]+rem
            rem=a//10
            a=a%10
            z.append(a) 
    if rem>0:
        z.append(rem)
    print (z)


addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
addTwoNumbers([2,4,3],[5,6,4])