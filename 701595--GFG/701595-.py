class Solution:
    def reverseString(self, s: str) -> str:
        
        # return s[::-1]
        
        
        reverse = ""
        l = len(s)
        for i in range(l - 1, -1, -1):
            reverse = reverse + s[i]
        return reverse

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna