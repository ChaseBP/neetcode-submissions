class TimeMap:

    def __init__(self):
        self.db = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #db structure 
        # {key1: [(value1,timestamp1),(value1,timestamp2),...,(valueN,timestampN)]}
        if key not in self.db:
            self.db[key] = [(value, timestamp)]
        else:
            self.db[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #fetch match from db
        if key not in self.db:
            return ""
        result = self.db[key]
        #print(result)
        # if no entries itself return ""
        #if not result:
            #return ""
        ans = ""
        # perform binary search
        left, right = 0, len(result) - 1

        while left <= right:
            mid = (left+right)//2
            #Check if timestamp matches -> return value
            if result[mid][1] == timestamp:
                return result[mid][0]
            #print(result[mid][1])
            if result[mid][1] < timestamp:
                ans = result[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        # If no value found return ""
        return ans
