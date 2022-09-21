"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        stack = [head]
        p = None
        while stack:
            cur = stack.pop()
            if p:
                p.next = cur
                cur.prev = p
            
            p = cur
            
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
        
        return head