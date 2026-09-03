class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        hashmap = {
            ']':'[', 
            '}':'{',
            ')':'('
        }
        for c in s:
            if c in "([{":
                lst.append(c)
            elif c in ")}]":
                if len(lst) > 0:
                    item = lst.pop()
                    if hashmap[c] == item:
                        continue
                    return False
                else:
                    return False
        if len(lst):
            return False
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna