class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set()
        for i in range(len(words)):
            for word in words:
                if (word != words[i]) and (word in words[i]):
                    output.add(word)
        return list(output)