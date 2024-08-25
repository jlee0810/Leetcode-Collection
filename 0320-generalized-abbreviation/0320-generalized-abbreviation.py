class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        n = len(word)

        def backtrack(idx, current):
            if idx == n:
                current_word = []
                abb = 0

                for i in range(n):
                    if current[i] == '*':
                        abb += 1
                    else:
                        if abb > 0:
                            current_word.append(str(abb))
                            abb = 0
                        current_word.append(word[i])
                if abb > 0:
                    current_word.append(str(abb))

                result.append("".join(current_word))
                return

            current.append(word[idx])
            backtrack(idx + 1, current)
            current.pop()

            current.append('*')
            backtrack(idx + 1, current)
            current.pop()

        backtrack(0, [])

        return result