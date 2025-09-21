# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
	def swapPairs(self,head):
		"""
		:typehead:Optional[ListNode]
		:rtype:Optional[ListNode]
		"""
		temp=ListNode(0)
		temp.next=head
		prev=temp

		while head and head.next:
			first=head
			second=head.next
			prev.next=second
			first.next=second.next
			second.next=first
			prev=first
			head=first.next
		return temp.next



