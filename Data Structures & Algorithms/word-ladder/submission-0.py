class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
      return 0

    if beginWord not in wordList:
      wordList.append(beginWord)
    # maps wildcard characters to the words in the list
    # *at -> [bat, cat]

    neighbours = {}

    for word in wordList:
      for i in range(len(word)):
        pattern = word[:i] + "*" + word[i + 1 :]
        if pattern not in neighbours:
          neighbours[pattern] = []

        neighbours[pattern].append(word)

    queue = deque([beginWord])
    visited = set([beginWord])

    changes = 1
    while queue:
        for _ in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return changes
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]

                for nextWord in neighbours.get(pattern, []):
                    if nextWord not in visited:
                        visited.add(nextWord)
                        queue.append(nextWord)
        changes += 1
    
    return 0
