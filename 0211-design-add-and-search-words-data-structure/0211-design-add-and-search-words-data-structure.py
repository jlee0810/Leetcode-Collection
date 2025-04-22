class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, search):
            if not node:
                return False
            if search == "":
                return node.end

            if search[0] == ".":
                for c in node.children.keys():
                    if dfs(node.children[c], search[1:]):
                        return True
                return False
            else:
                c = search[0]
                if c not in node.children:
                    return False
                else:
                    return dfs(node.children[c], search[1:])

        return dfs(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)