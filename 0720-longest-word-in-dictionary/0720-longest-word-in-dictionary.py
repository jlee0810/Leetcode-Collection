class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.end = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))
        
        root = Trie()
        longest = ""

        for word in words:
            root.addWord(word)
            curr = root.root

            valid = True
            for i in range(len(word)):
                if word[i] not in curr.child or not curr.child[word[i]].end:
                    valid = False
                    break
                curr = curr.child[word[i]]
                
            if valid and len(word) > len(longest):
                longest = word
                
        return longest
