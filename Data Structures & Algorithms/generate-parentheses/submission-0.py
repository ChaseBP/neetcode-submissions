class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(path,oc,ec):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            if oc < n:
                path.append("(")
                helper(path,oc+1,ec)
                path.pop()
            
            if ec < oc:
                path.append(")")
                helper(path,oc,ec+1)
                path.pop()
        
        helper([],0,0)
        return res


