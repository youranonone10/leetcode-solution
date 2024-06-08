class Solution:
    def checkSubarraySum(self, nums, k):
        # Dictionary to store the first occurrence of a remainder
        remainder_map = {0: -1}  # Initialize with remainder 0 at index -1
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k

            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i

        return False

# Example usage:
sol = Solution()
print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))  # Output: True
print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))  # Output: True
print(sol.checkSubarraySum([23, 2, 6, 4, 7], 13))  # Output: False
