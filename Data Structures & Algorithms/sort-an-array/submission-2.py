class Solution:
    def partition(self, arr, left: int, right: int):
        
        mid = (left + right) // 2

        if arr[left] > arr[mid]:
            arr[left], arr[mid] = arr[mid], arr[left]
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[mid] > arr[right]:
            arr[mid], arr[right] = arr[right], arr[mid]
        
        arr[mid], arr[right] = arr[right], arr[mid]
        
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1

    def sortArray(self, nums: List[int]) -> List[int]:
        # Stack to store the [left, right] ranges to be sorted
        stack = []
        
        # Initial range
        stack.append((0, len(nums) - 1))
        
        while stack:
            left, right = stack.pop()
            
            if left < right:
                # Partition the array and get the pivot index
                pivot_idx = self.partition(nums, left, right)
                
                # Push the right side range to stack
                if pivot_idx + 1 < right:
                    stack.append((pivot_idx + 1, right))
                
                # Push the left side range to stack
                if left < pivot_idx - 1:
                    stack.append((left, pivot_idx - 1))
        return nums