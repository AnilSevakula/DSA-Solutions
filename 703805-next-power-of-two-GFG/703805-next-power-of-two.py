class Solution:
    def nextPowerOfTwo(self, n):
        s = 0
        temp = n
        while temp > 0:
            if temp & 1 == 1:
                s += 1
            temp = temp >> 1
        if s == 1:
            return n
        pos = 0
        while n > 0:
            n = n >> 1
            pos += 1
        return 2**(pos)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna