class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map value to its index in inorder array for O(1) lookups
        in_map = {val: i for i, val in enumerate(inorder)}
        
        # Pointer for the current root in postorder array
        post_idx = len(postorder) - 1
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal post_idx
            if in_left > in_right:
                return None
            
            # The last element in current postorder range is the root
            root_val = postorder[post_idx]
            root = TreeNode(root_val)
            
            # Move pointer to the next root element
            post_idx -= 1
            
            # Get root index in inorder array to divide subtrees
            index = in_map[root_val]
            
            # Build right subtree first because postorder processes left, right, root
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root
            
        return helper(0, len(inorder) - 1)