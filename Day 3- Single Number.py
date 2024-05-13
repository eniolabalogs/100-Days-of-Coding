def singleNumber(nums):
    result=0
    for x in nums:
        result ^=x
    return result
    """
    c=[]
    for x in nums:
        if x not in c:
            c.append(x)
        else:
            c.remove(x)
    return (c[0])
    """
print(singleNumber([2,2,1]))