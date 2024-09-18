class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, s):
            if node.end and len(s) == 0:
                return True
            if len(s) == 0:
                return False

            for idx, c in enumerate(s):
                if c == '.':
                    for child in node.child:
                        if dfs(node.child[child], s[idx + 1 : ]):
                            return True
                    return False
                if c not in node.child:
                    return False
                else:
                    return dfs(node.child[c], s[idx + 1 : ])
                    
        return dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)