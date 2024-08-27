class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False 

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> TrieNode:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.end = True
        return curr

    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        nodes = {}
        for word in words:
            node = self.addWord(word[::-1])
            nodes[node] = len(word) + 1

        total_length = 0
        for node, length in nodes.items():
            if len(node.child) == 0:
                total_length += length
        
        return total_length
