# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        good_nodes = 0

        def pre_order(node: TreeNode, curr_max: int):
            nonlocal good_nodes

            if not node:
                return
            print("val: ", node.val)
            
            if node.val >= curr_max:
                print("adding")
                good_nodes += 1
                curr_max = node.val

            pre_order(node.left, curr_max)
            pre_order(node.right, curr_max)

            # if node.left:
            #     if node.left.val >= root.val and node.left.val >= node.val:
            #         print("node.left.val: ", node.left.val)
            #         good_nodes += 1
            #     pre_order(node.left)

            # if node.right:
            #     if node.right.val >= root.val and node.right.val >= node.val:
            #         print("node.right.val: ", node.right.val)
            #         good_nodes += 1
            #     pre_order(node.right)


        pre_order(root, root.val)

        return good_nodes