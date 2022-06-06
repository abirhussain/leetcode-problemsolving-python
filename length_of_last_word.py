class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        prev_word_count = 0
        pres_word_count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if pres_word_count != 0:
                    prev_word_count = pres_word_count
                pres_word_count = 0
            else:
                pres_word_count = pres_word_count + 1
        if pres_word_count != 0:
            return pres_word_count
        else:
            return prev_word_count
