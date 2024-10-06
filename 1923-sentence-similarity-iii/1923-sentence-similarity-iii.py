class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        
        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")

        i, j = 0, 0
        while i < len(sentence2) and sentence1[i] == sentence2[i]:
            i += 1
        
        while j < len(sentence2) and sentence1[-j-1] == sentence2[-j-1]:
            j += 1

        return i + j >= len(sentence2)
