class Solution:
    def subarraysDivByK(self, nums, k):
        prefix_sum = 0
        remainder_count = {0: 1}
        count = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # Python's modulo operator can return negative results, adjust to be positive
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        return count
