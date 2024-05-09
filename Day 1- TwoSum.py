'''
def TwoSum(n,t):
    for i in range((len(n)-1)):
        if n[i]+ n[i+1]==t:
            print (i,i+1)

TwoSum([3,3],(6))
'''

"""
def TwoSum(n,t):
    for i in n:
        diff= t-i 
        if diff in n:
            print (diff, i)
TwoSum([2,7,11,15],(9))    
"""

def TwoSum(n,t):
    diction={}
    for i, a in enumerate(n):
        d= t- a
        if d in diction:
            return [diction[d],i]
        else:
            diction[a]=i

print(TwoSum(([2,7,11,15]),(9)))