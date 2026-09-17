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
        required = len(t_count)
        formed = 0
        
        # Left and Right pointers
        left, right = 0, 0
        
        # ans tuple: (window_length, left_pointer, right_pointer)
        ans = float("inf"), None, None
        
        while right < len(s):
            character = s[right]
            window_count[character] = window_count.get(character, 0) + 1
            
            # If the frequency of the current character matches its required frequency in t
            if character in t_count and window_count[character] == t_count[character]:
                formed += 1
            
            # Try to contract the window from the left if it's valid
            while left <= right and formed == required:
                character = s[left]
                
                # Save the smallest window so far
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # The character at 'left' position is no longer a part of the window
              
