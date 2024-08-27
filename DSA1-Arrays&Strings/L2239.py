# 2239. Find Closest Number to Zero

''' Plan: 
For each number calculate the distance
  if the distance is less than what is stored
    then replace both the distance and the number

  if distance is the same
    then replace the number with the largest of the two numbers

** Essentially we want the CLOSEST number first, and if two or more numbers are 
  close then we want the largest of them all. 

'''
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        d = float('inf')
        for n in nums: 
            distance = abs(n)
            if distance < d: 
                d = distance
                l = n
            elif d == distance and n > l: 
                l = n

        return l


# Time Complexity : O(N) , N being the numbers in the list
# Space Complexity: O(1)