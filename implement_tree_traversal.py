# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        """
        Preorder: Root -> Left -> Right
        """
        # TODO: implement logic here
        if root is None:
          return [] 

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


    def inorderTraversal(self, root: TreeNode):
        """
        Inorder: Left -> Root -> Right
        """
        # TODO: implement logic here
        if root is None:
          return []


        self.inorderTraversal(root.left)
        print("Val:",root.val)
        self.inorderTraversal(root.right)

        return []

    def postorderTraversal(self, root: TreeNode):
        """
        Postorder: Left -> Right -> Root
        """
        # TODO: implement logic here

        if root is None:
          return []

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print("Val: ",root.val)

        return []

    def levelOrderTraversal(self, root: TreeNode):
        """
        Level Order: Traverse level by level
        """
        # if root is None:
        #     return []

        # result = []
        # queue = deque([root])   # start with root in queue

        # while queue:
        #     level = []
        #     size = len(queue)   # number of nodes at this level

        #     for _ in range(size):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         if node.left:
        #           queue.append(node.left)
        #         if node.right:
        #           queue.append(node.right)

        #     result.append(level)

        # return result


        if root is None:
          return []

        result = []
        queue = deque([root])

        while queue:
          level=[]
          n = len(queue)

          for _ in range(n):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
          
          result.append(level)
          
        return result


