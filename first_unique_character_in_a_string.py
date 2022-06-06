class Solution:
    def firstUniqChar(self, s: str) -> int:
        chararcter_frequencies = {}
        for character in s:
            chararcter_frequencies[character] = chararcter_frequencies.get(character, 0) + 1
        for i in range(len(s)):
            character = s[i]
            if chararcter_frequencies[character] == 1:
                return i
        return -1
            
