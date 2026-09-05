class Solution:
    def nextPowerOfTwo(self, n):
        power = 1
        while power < n:
            power *= 2
        return power
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna