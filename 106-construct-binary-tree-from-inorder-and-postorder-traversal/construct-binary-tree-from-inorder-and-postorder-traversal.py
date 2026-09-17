class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map value to its index in inorder array for O(1) lookups
        in_map = {val: i for i, val in enumerate(inorder)}
        
        # Pointer for the current root in postorder array
        post_idx = len(postorder) - 1
   
           
