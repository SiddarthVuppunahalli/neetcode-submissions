class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        back = len(s) - 1
        front = 0

        while (front != back) and front < len(s):
            if not s[front].isalnum():
                front += 1
            elif not s[back].isalnum():  
                back -= 1
            elif s[front] != s[back]:
                return False
            else:
                front += 1
                back -= 1

        return True