class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for stri in strs:
            temp = ""
            i = 0
            while i < min(len(prefix),len(stri)) and prefix[i] == stri[i]:
                temp += stri[i]
                i+=1
            prefix = temp


        return prefix