class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word=sentence.split()
        if word[0][0]!=word[-1][-1]:
            return False
        for i in range(len(word)-1):
            if word[i][-1]!=word[i+1][0]:
                return False
        return True

    
