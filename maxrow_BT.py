###
# Approach:
# - Use BFS (level-order traversal) to explore the tree level by level.
# - For each level, keep track of the maximum value seen so far.
# - After processing all nodes at a level, add that max value to the result.
#
# Time Complexity: O(n), where n is number of nodes
# Space Complexity: O(w), where w is the max width (max nodes at any level)
###
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        if not root:
            return []
        result = []
        max_level = float('-inf')
        queue = deque()
        queue.append(root)
        
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                max_level = max(max_level, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(max_level)
        return result
    
    def main(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(9)

        output = self.largestValues(root)
        print("Largest values in each row:", output)
        # Expected: [1, 3, 9]

# Run
sol = Solution()
sol.main()