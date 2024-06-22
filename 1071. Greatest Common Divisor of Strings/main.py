class Solution:
    def gcdOfStrings(self, str1, str2):
        # Helper function to find the greatest common divisor of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Check if s1 can be constructed by repeating s2
        def check(s1, s2):
            if len(s1) % len(s2) != 0:
                return False
            repeat = len(s1) // len(s2)
            return s1 == s2 * repeat
        
        # Find the gcd of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # Candidate substring is the substring of str1 with length gcd_length
        candidate = str1[:gcd_length]
        
        # Check if candidate divides both str1 and str2
        if check(str1, candidate) and check(str2, candidate):
            return candidate
        else:
            return ""

# Example cases
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB")) # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))   # Output: ""
print(solution.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")) # Output: "TAUXX"
