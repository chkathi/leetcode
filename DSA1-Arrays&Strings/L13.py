# 13. Roman to Integer
'''
Add all values that are mapped, but
  ONLY subtract when the next value is greater than the current
    ** make sure the net value is within the array
'''
class Solution:
    def romanToInt(self, s: str) -> int:
      dt = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
      }

      total = 0
      for i in range(0, len(s)):
        cur = s[i]
        a = dt[cur]

        b = 0
        if i + 1 < len(s): 
            cur2 = s[i + 1]
            b = dt[cur2]
    
        if a < b:
          total -= a
          continue
      
        total += a

      return total