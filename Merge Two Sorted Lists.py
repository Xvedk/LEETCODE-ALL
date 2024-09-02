# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # suppose first linked list is empty, directly return the second linked list
        if list1 == None:
            return list2
        # suppose second linked list is empty, directly return the first linked list
        if list2 == None:
            return list1
        # if both lists are empty, return 
        if list1 == None and list2 == None:
            return  

        temp1 = list1
        temp2 = list2
        while temp1.next != None:
            temp1 = temp1.next

        temp1.next = temp2

        tempList = []
        pointer = list1

        while pointer:
            tempList.append(pointer.val)
            pointer = pointer.next

        tempList.sort()
        i = 0
        pointer = list1
        while pointer:
            pointer.val = tempList[i]
            i = i + 1
            pointer = pointer.next

        return list1
        
