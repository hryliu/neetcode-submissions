class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # root.val == key: this is the node to delete
            if not root.left and not root.right:
                return None              # 0 children
            elif not root.right:
                return root.left         # 1 child (left only) -> promote it
            elif not root.left:
                return root.right        # 1 child (right only) -> promote it
            else:
                # 2 children: copy predecessor (max of left subtree) up,
                # then delete that duplicate from the left subtree
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                root.val = predecessor.val
                root.left = self.deleteNode(root.left, root.val)

        return root