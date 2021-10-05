class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        left_idx, right_idx = 0, len(height)-1 
        right_height, left_height = height[right_idx], height[left_idx]
        
        while left_idx < right_idx:
            left_height, right_height = max(left_height, height[left_idx]), max(right_height, height[right_idx])
            if left_height <= right_height:
                count += left_height - height[left_idx]
                left_idx += 1
            else:
                count += right_height - height[right_idx]
                right_idx -= 1
        return count
        
        