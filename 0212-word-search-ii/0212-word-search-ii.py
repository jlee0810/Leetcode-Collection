
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWords(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        
        root = TrieNode()
        for word in words:
            root.addWords(word)

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or board[r][c] not in node.children:
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                result.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return result
