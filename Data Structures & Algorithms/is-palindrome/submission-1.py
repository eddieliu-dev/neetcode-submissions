class Solution:
    def isPalindrome(self, s: str) -> bool:
        adjusted_s = "".join(ch for ch in s if ch.isalnum()).lower()

        front = 0
        back = len(adjusted_s)-1

        for _ in range(len(adjusted_s)//2):
            if adjusted_s[front] != adjusted_s[back]:
                return False
            front += 1
            back -= 1
        return True
