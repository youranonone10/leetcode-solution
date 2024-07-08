class Solution:
    def findTheWinner(self, n, k):
        winner = 0  # Since we start counting from 0 in the iterative method
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1  # Adjusting the index to match the 1-based indexing

# Example usage
solution = Solution()
print(solution.findTheWinner(5, 2))  # Output: 3
print(solution.findTheWinner(6, 5))  # Output: 1
