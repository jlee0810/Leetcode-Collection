class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end_of_word = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def insert_word(word):
            node = root
            for char in word:
                if char not in node.child:
                    node.child[char] = TrieNode()
                node = node.child[char]
            node.is_end_of_word = True
        
        def can_form(word, node, start, count):
            if start == len(word):
                return count > 1
            
            current_node = node
            for i in range(start, len(word)):
                if word[i] not in current_node.child:
                    return False
                current_node = current_node.child[word[i]]
                if current_node.is_end_of_word:
                    if can_form(word, root, i + 1, count + 1):
                        return True
            return False
        
        root = TrieNode()
        
        words.sort(key=len)
        
        concatenated_words = []
        
        for word in words:
            if not word:
                continue
            if can_form(word, root, 0, 0):
                concatenated_words.append(word)
            else:
                insert_word(word)
        
        return concatenated_words
