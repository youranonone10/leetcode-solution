class Solution:
    def longestPalindrome(self, s):
        from collections import Counter
        
        # Count frequency of each character
        char_count = Counter(s)
        
        length_of_palindrome = 0
        odd_count_found = False
        
        for count in char_count.values():
            if count % 2 == 0:
                length_of_palindrome += count
            else:
                length_of_palindrome += count - 1
                odd_count_found = True
        
        # If any character has an odd count, we can add one more to the palindrome length
        if odd_count_found:
            length_of_palindrome += 1
        
        return length_of_palindrome

# Example Usage
sol = Solution()
print(sol.longestPalindrome("abccccdd"))  # Output: 7
print(sol.longestPalindrome("a"))         # Output: 1
