class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

class Solution:
    def traverse_trie(self, node, curr_word):
        level = 0
        for ch in curr_word:
            if ch not in node.children:
                return level
            level += 1
            node = node.children[ch]
        return level

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))

        res = 0
        for num in arr2:
            level = self.traverse_trie(trie.root, str(num))
            res = max(res, level)

        return res