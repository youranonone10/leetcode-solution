class Solution:
    def heightChecker(self, heights):
        # Step 1: Create the expected array by sorting the heights array
        expected = sorted(heights)
        
        # Step 2: Initialize a counter for the number of mismatches
        mismatch_count = 0
        
        # Step 3: Compare each element in heights and expected
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1
        
        # Step 4: Return the number of mismatches
        return mismatch_count

# Example usage:
sol = Solution()
print(sol.heightChecker([1,1,4,2,1,3]))  # Output: 3
print(sol.heightChecker([5,1,2,3,4]))    # Output: 5
print(sol.heightChecker([1,2,3,4,5]))    # Output: 0
