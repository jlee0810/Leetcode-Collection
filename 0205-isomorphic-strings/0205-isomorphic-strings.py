class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_translate = []
        t_translate = []

        s_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_translate.append(s_dict[s[i]])
            else:
                s_translate.append(i)
                s_dict[s[i]] = i
        
        t_dict = {}
        for i in range(len(t)):
            if t[i] in t_dict:
                t_translate.append(t_dict[t[i]])
            else:
                t_translate.append(i)
                t_dict[t[i]] = i

        return s_translate == t_translate