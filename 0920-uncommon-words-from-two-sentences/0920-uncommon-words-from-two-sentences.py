class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1 = Counter(s1.split(" "))
        lst2 = Counter(s2.split(" ")) 

        uncommon = []
        for word in lst1:
            if lst1[word] == 1 and word not in lst2:
                uncommon.append(word)

        for word in lst2:
            if lst2[word] == 1 and word not in lst1:
                uncommon.append(word)
        
        return uncommon