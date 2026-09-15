class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        l = 0
        r = len(s) - 1
        sLower = s.lower()

        while r > l:

            while (r > l) and (sLower[l] not in alphabet):
                l += 1
            while (r > l) and (sLower[r] not in alphabet):
                r -= 1

            if sLower[l] != sLower[r]:
                return False
        
            l, r = l + 1, r - 1
        return True
    