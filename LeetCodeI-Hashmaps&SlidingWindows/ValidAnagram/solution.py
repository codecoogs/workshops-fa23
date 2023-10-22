class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        mp_s = {}

        for i in range(len(s)):
            if s[i] not in mp_s:
                mp_s[s[i]] = 1
            else:
                mp_s[s[i]] += 1

        mp_t = {}
        for i in range(len(t)):
            if t[i] not in mp_t:
                mp_t[t[i]] = 1
            else:
                mp_t[t[i]] += 1

        return mp_s == mp_t
        