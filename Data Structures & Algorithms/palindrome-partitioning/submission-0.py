class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        def dfs(index,path):
            if index == len(s):
                res.append(path.copy())
                return
            
            for i in range(index, len(s)):
                # Is current word a palindrome?
                if isPalindrome(index, i):
                    path.append(s[index: i+1])
                    dfs(i+1,path)
                    path.pop()
        dfs(0,[])
        return res


            