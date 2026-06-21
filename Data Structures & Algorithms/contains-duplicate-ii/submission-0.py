class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        
        if k < 1:
            return False
        
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            print(R, L)

            if nums[R] in window:
                return True
            window.add(nums[R])
        
        return False