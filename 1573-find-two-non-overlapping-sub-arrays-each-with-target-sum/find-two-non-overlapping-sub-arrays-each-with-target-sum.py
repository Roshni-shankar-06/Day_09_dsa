class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1
        best = [INF] * n
        left = 0
        window_sum = 0
        min_len = INF
        result = INF
        
        for right in range(n):
            window_sum += arr[right]
            
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
                
            if window_sum == target:
                length = right - left + 1
            
           
