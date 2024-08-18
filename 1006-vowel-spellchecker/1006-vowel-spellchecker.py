class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(string):
            new_s = ""
            for c in string:
                if c in ["a", "e", "i", "o", "u"]:
                    new_s += "*"
                else:
                    new_s += c
            return new_s

        words_match = set(wordlist)
        words_no_cap = {}
        words_vowel = {}

        for word in wordlist:
            word_lower = word.lower()
            if word_lower not in words_no_cap:
                words_no_cap[word_lower] = word
            word_devowel = devowel(word_lower)
            if word_devowel not in words_vowel:
                words_vowel[word_devowel] = word

        result = []
        for query in queries:
            if query in words_match:
                result.append(query)
                continue
            query_lower = query.lower()
            if query_lower in words_no_cap:
                result.append(words_no_cap[query_lower])
                continue
            query_lower_devowel = devowel(query_lower)
            if query_lower_devowel in words_vowel:
                result.append(words_vowel[query_lower_devowel])
                continue
            result.append("")
        
        return result






