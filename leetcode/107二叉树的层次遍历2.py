#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        stacks = []
        new_stack = [root]
        stacks.append(new_stack)

        while new_stack != []:
            new_stack_2 = []
            for i in new_stack:
                if i.left is None and i.right is None:
                    continue
                if i.left is not None:
                    new_stack_2.append(i.left)
                if i.right is not None:
                    new_stack_2.append(i.right)
            new_stack = new_stack_2
            stacks.append(new_stack)
        stacks.pop()

        results = []
        for stack in stacks:
            result = []
            for _ in stack:
                result.append(_.val)
            results.append(result)
        return results[::-1]

if __name__ == '__main__':
    tree = [3,9,20,null,null,15,7]
    a =Solution()
    a.levelOrderBottom()