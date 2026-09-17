from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        # Frequency map for characters in t
        t_count = Counter(t)
        # Dictionary to keep track of characters in the current window
        window_count = {}
        
        # 'required' is the number of unique characters in t that must be present in the window
        # 'formed' tracks how many unique characters meet their target frequency requirement
      
  
