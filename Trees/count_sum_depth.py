# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countofnodes(self,root):

      if root is None:
        return 0

      return 1 + self.countofnodes(root.left) + self.countofnodes(root.right)

    def sumofnodes(self,root):

      if root is None:
        return 0

      return root.val + self.sumofnodes(root.left) + self.sumofnodes(root.right)


    def heightoftree(self,root):

      if root is None:
        return 0
      
      return 1 + max(self.heightoftree(root.left), self.heightoftree(root.right))

