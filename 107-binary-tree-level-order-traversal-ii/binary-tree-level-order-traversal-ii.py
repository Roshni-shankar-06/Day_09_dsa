from collections import deque
from typing import List, Optional


class Solution:

  def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    result = []
    queue = deque([root])

    while queue:
      level_size = len(queue)
    
     
   
