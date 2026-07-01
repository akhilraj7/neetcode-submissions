import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-zA-Z0-9 ]', '', s)
        s = s.replace(" ", "")
        s = s.lower()

        out_text = s[::-1]

        print(s, out_text)

        if s == out_text:
            return True
        else:
            return False        