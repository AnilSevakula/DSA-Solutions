class Solution:
    def nextPowerOfTwo(self, n):

        if n <= 1:
            return 1

        # Decrement n by 1.
        n -= 1

        # Propagate the most significant set bit to all lower positions.
        n |= (n >> 1)
        n |= (n >> 2)
        n |= (n >> 4)
        n |= (n >> 8)
        n |= (n >> 16)

        # Return the next power of 2.
        return n + 1


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna