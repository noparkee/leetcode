class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        len1 = len(s)
        len2 = len(t)

        s.sort()
        t.sort()

        if len1 != len2:
            a = False
    
        cnt = 0
        for i, j in zip(s, t):
            if i == j:
                cnt += 1
            else:
                return False

        if cnt == len1 and cnt == len2:
            return True
        else:
            return False

# Collection 사용할 수도
# 그냥 sorted로만 비교해도