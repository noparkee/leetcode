class Solution:
    def sortString(self, s: str) -> str:
        a = list(s)

        r = []
        while len(a) > 0:
            
            temp = list(set(a))
            temp = sorted(temp)
            r = r + temp
            for i in temp:
                a.remove(i)
            temp = list(set(a))
            temp = sorted(temp, reverse=True)
            r = r + temp
            for i in temp:
                a.remove(i)

        return ''.join(r)

''' <use less memory>
class Solution:
    def sortString(self, s: str) -> str:
      result = ''
      chl = set() 
      for i in s:
        chl.add(i)
      
      chl = list(chl)
      chl.sort()
      
      while s:
        for i in chl:
          if s != s.replace(i,'',1):
            s = s.replace(i,'',1)
            result += i
        for i in chl[::-1]:
          if s != s.replace(i,'',1):
            s = s.replace(i,'',1)
            result += i
      return result'''