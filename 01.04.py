from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = [0] * 1000
        for c in s:
            count[ord(c)] = (count[ord(c)] + 1) % 2
        count_odd = 0
        for i in count:
            count_odd += i
            if count_odd > 1:
                return False
        return True
    
    def canPermutePalindrome2(self, s: str) -> bool:
        count = Counter(s).values()
        count_odd = 0
        for c in count:
            count_odd += c & 1
            if count_odd > 1:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.canPermutePalindrome2('tactcoa'))