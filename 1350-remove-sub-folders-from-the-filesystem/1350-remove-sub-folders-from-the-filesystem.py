class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.child = {}
        self.end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()

        for f in folder:
            curr = root
            for name in f.split("/")[1:]:
                if name not in curr.child:
                    curr.child[name] = TrieNode(name)
                curr = curr.child[name]
            curr.end = True

        result = []
        for f in folder:
            isSubFolder = False
            curr = root
            for name in f.split('/')[1:-1]:
                curr = curr.child[name]
                if curr.end:
                    isSubFolder = True
                    break
            if not isSubFolder:
                result.append(f)

        return result