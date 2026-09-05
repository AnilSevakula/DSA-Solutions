class Solution:
    def checkString(self, s):
        v = 0
        c = 0
        vowels = 'aeiou'
        for ch in s:
            if ch in vowels:
                v  += 1
            else:
                c += 1
        if v == c:
            print("Same")
        elif v > c:
            print("Yes")
        else:
            print("No")

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna