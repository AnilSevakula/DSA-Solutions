class Solution:
    def countNonRepeated(self,arr):
        h = {}
        for num in arr:
            h[num] = h.get(num, 0) + 1
        count = 0
        for num in h:
            if h[num] == 1:
                count += 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna