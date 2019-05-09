# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import null as null


class Solution:
    def maxDepth(self, root):
        """递归
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

    def maxDepth(self, root):
        """
        :type root: TreeNode迭代
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth
if __name__ == '__main__':
    tree =[3,9,20,null,null,15,7]
    a = Solution()
    b= Solution()
    f1=a.maxDepth(tree)
    f2=b.maxDepth(tree)
    print(f1,f2)