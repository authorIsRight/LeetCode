"""2. Add Two Numbers
Medium
27.5K
5.3K
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""

from typing import Optional
import json
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val

    def reversed_and_int(self):

        as_string = ""

        for i in self.val[::-1]:
            as_string += str(i)
        return int(as_string)


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return l1+l2


def read_input():

    l1 = json.loads(input())
    l2 = json.loads(input())
    return l1, l2


if __name__ == "__main__":
    l1, l2 = read_input()

    obj1 = ListNode(l1)
    obj2 = ListNode(l2)

    solution = Solution()

    print(solution.addTwoNumbers(obj1.reversed_and_int(), obj2.reversed_and_int()))    

