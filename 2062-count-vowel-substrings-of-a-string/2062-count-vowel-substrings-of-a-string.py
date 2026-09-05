class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        i = 0
        count =0
        vowels = 'aeiou'
        for i in range(len(word)):
            seen = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count += 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna