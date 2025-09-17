class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c != word[i]:
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordSet and newWord not in visited:
                            visited.add(newWord)
                            q.append((newWord, step + 1))
        return 0

