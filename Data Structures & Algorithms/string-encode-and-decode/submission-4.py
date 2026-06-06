class Solution:
    def encode(self, strs: List[str]) -> str:
        finalString = ""

        for string in strs:
            strLength = str(len(string))
            currentEncodedString = strLength + "#" + string

            finalString = finalString + currentEncodedString

        return finalString

    def decode(self, string: str) -> List[str]:
        decodedString = []

        i = 0
        while i < len(string):
            j = i
            while string[j] != "#":
                j += 1
            strLen = int(string[i:j])

            i = j + 1
            stringSlice = string[i : i + strLen]
            decodedString.append(stringSlice)
            i += strLen
        return decodedString
