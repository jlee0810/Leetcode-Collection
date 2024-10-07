class Solution:
    def minLength(self, s: str) -> int:
        def dfs(sub):
            if "AB" not in sub and "CD" not in sub:
                return len(sub)
            
            if "AB" in sub:
                index = sub.find("AB")
                new_sub = sub[:index] + sub[index + 2:]
                return dfs(new_sub)
            
            if "CD" in sub:
                index = sub.find("CD")
                new_sub = sub[:index] + sub[index + 2:]
                return dfs(new_sub)
        
        return dfs(s)
