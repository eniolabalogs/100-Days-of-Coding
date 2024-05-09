def reverse(lst):
    if lst==[]:
        return ([])
    return ([lst.pop()]+ reverse(lst))
print(reverse([2,4,5,6,8]))