class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            current_word, level = q.popleft()
            for i in range(len(current_word)):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        q.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
