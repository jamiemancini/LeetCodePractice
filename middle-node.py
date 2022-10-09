#876. Middle of the Linked List

#Given the head of a singly linked list, return the middle node of the linked list.

#If there are two middle nodes, return the second middle node

#Input: head = [1,2,3,4,5]
#Output: [3,4,5]
#Explanation: The middle node of the list is node 3.

#Explanation from the Video:
#Linked lists consist of a NODE and a POINTER that points to the next NODE
#With Linked lists we cannot use the method len to find the length
#We must go through the entire list?

#1 find the length of the linked list by iterating through the list
#2 find the middle of the linked list
######if the linked list is an odd number then the middle node will 1 node
######if the linked list is an even number then the middle node will 2 nodes,
######and we will need to return the 2nd


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution:
    def middleNode(self, head):
        len_list = 0
        start = node = head
        while start:
            len_list += 1
            start = start.next
        middle = len_list // 2

        counter = 0
        while node:
            if counter == middle:
                return node
            else:
                counter += 1
                node=node.next
        return None