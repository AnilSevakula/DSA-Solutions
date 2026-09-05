class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in range(97, 97+26):
            d[chr(i)] = 0

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch in t:
            d[ch] = d.get(ch, 0) - 1

        for ch in d:
            if d[ch] != 0:
                return False
        else:
            return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna