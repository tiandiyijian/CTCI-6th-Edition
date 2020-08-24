class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) == len(second):
            diff = 0
            for a, b in zip(first, second):
                if a != b:
                    diff += 1
                    if diff > 1:
                        return False
            return diff <= 1
        elif abs(len(first) - len(second)) == 1:
            flag = False
            if len(first) < len(second):
                first, second = second, first
            i = j = 0
            while i < len(first) and j < len(second):
                if first[i] != second[j]:
                    if not flag:
                        flag = True
                        i += 1
                    else:
                        return False
                else:
                    i += 1
                    j += 1
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.oneEditAway('mart', 'karma'))
