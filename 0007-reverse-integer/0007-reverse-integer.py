class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x = str(x)
        if is_neg:
            x = x[len(x)-1:0:-1]
            x = int(x)
            x = -x

        else:
            x = x[::-1]
            x = int(x)
        if x < -2**31 or x > 2**31 -1:
            return 0
        return x

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna