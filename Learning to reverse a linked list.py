"""
def reverse(lst):
    if lst==[]:
        return ([])
    return ([lst.pop()]+ reverse(lst))
print(reverse([2,4,5,6,8]))
"""

"""
def append(data):
    new_node=node(data)
    cur=node()
    while cur.next!=None:
        cur=cur.next
    cur.next=new_node

append(1)
"""
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()
    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+= 1
            cur=cur.next
        return total
    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node!=None:
            elems.append(cur_node.data)
            cur_node=cur_node.next
             ZX.AERSDPprint (elems)

my_list= linked_list()
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.display()
    

         