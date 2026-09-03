class Solution:
    def countBitsFlip(self, a, b):
        count = 0
        while a or b:
            last_a = a & 1
            last_b = b & 1
            
            count += last_a ^ last_b
            
            a = a >> 1
            b = b >> 1
            
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna