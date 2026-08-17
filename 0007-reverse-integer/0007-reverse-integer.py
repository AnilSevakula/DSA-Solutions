class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        if is_negative:
            x = -x
        num = 0
        while x > 0:
            rem = x % 10
            num = num *10 + rem
            x //= 10
        num = - num if is_negative else num
        if num >=  2**31 - 1 or num <= -2**31:
            return 0
        return num

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna