class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + '#' + string
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])
            #Move 'i' to the start of the string
            i = j + 1

            curr_str = s[i : i+length]
            result.append(curr_str)

            i += length
        return result 

            