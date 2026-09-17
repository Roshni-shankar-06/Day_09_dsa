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
                if left > 0 and best[left - 1] != INF:
                    result = min(result, length + best[left - 1])
                min_len = min(min_len, length)
                best[right] = min_len
            else:
                if right > 0:
                    best[right] = best[right - 1]
                    
        return -1 if result == INF else result
