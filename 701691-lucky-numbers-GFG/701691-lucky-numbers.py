class Solution:
    def isLucky(self, n): 
        # Time Complexity: O(sqrt(n)) - The loop runs until i exceeds the current position.
        # Space Complexity: O(1) - No extra space used.
        # This implementation is correct and optimal for the Lucky Number logic.
        i = 2
        pos = n
        while i <= pos:
            if pos % i == 0:
                return False
            pos = pos - pos//i
            i += 1
        return True
        # Your solution is correct! You can now click the "Submit" button on GFG.
        # After passing, LeetHub will automatically sync this to your GitHub repository.

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna