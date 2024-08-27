# 1768. Merge Strings Alternately
''' Plan: 
Two pointer approach

As long as both pointers are less then their word's length
  we alternatively add each letter

the while loops ends if we reach the end of one of the words

add remaining letters of the first or second word

'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        combine = ""

        while i < len(word1) and j < len(word2): 
            combine += word1[i]
            combine += word2[j]
            i += 1
            j += 1

        if i < len(word1): 
            for l in range(i , len(word1)):
                combine += word1[l]

        if j < len(word2):
            for l in range(j , len(word2)):
                combine += word2[l]

        return combine