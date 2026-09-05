class Solution:
    def longestUniqueSubstr(self, s):
        maxLength = 0
        
        for i in range(len(s)):
            harr = [0]*256
            for j in range(i, len(s)):
                if harr[ord(s[j])] == 1:
                    break
                l = j - i + 1
                maxLength = max(maxLength, l)
                harr[ord(s[j])] = 1
        return maxLength

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna