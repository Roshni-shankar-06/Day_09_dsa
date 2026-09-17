class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        in_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
           
            
         
            
       
