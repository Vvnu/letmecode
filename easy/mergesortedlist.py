class Listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def mergesorted(self,list1:Optional[Listnode],list2:Optional[listnode])->Optional[listnode]:
    if not list1:
        return list2
    if not list2:
        return list1:
    if list1.val< list2.val:
        list1.next=self.mergesorted(list1.next,list2)
        return list1
    else:
        list2.next=self.mergesorted(list1,list2.next)
        return list2