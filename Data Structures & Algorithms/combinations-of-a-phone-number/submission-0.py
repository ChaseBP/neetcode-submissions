class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []
    hp = {
      "2": "abc",
      "3": "def",
      "4": "ghi",
      "5": "jkl",
      "6": "mno",
      "7": "pqrs",
      "8": "tuv",
      "9": "wxyz",
    }

    res = []
    def dfs(index,path):
        if index == len(digits):
            res.append("".join(path.copy()))
            return
        letters = hp[digits[index]]
        for char in letters:
            path.append(char)
            dfs(index+1,path)
            path.pop()

    dfs(0,[])
    return res
        
