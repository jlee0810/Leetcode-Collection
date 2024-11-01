class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.isfolder = False
        self.childfolder = {}

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for f in folder:
            parse = f.split('/')
            parse = parse[1:]
            curr = root

            for name in parse:
                if name not in curr.childfolder:
                    curr.childfolder[name] = TrieNode(name)
                    curr = curr.childfolder[name]
                else:
                    curr = curr.childfolder[name]
            curr.isfolder = True
        
        result = []
        for f in folder:
            parse = f.split('/')
            parse = parse[1: - 1]
            curr = root

            issubfolder = False
            for name in parse:
                curr = curr.childfolder[name]
                if curr.isfolder:
                    issubfolder = True
                    break
            if (not issubfolder):
                result.append(f)
        
        return result
