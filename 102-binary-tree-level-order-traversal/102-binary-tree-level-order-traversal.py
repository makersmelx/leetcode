# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue, ret = deque([root]), []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                head = queue.popleft()
                level.append(head.val)
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            
            ret.append(level)
        return ret
                