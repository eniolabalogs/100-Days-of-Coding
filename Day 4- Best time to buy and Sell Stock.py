def maxProfit(prices):
    """
    n=prices[0]
    a=[]
    for i in prices:
        if i<n:
            n=i
            a=[]
            a.append(n)
            b=a.index(n)
                
        else:
            a.append(i)
    c=max(a)
    return c-n
    """

    a=[]
    for i in range(len(prices)-1):
        for j in range(len(prices)-1-i):
            a.append(prices[j+1+i]-prices[i])
    if max(a)<0:
        return 0
    else:
        return max(a)

print(maxProfit([1]))
