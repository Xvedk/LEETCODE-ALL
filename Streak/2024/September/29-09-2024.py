class AllOne:
    def _init_(self):
        self.dict = {}
        self.check = 0
        self.result = ""
    def inc(self, key: str) -> None:
        self.check = 0
        if (key in self.dict):
            self.dict[key] += 1
        else:
            self.dict[key] = 1
    def dec(self, key: str) -> None:
        self.check = 0
        if (self.dict[key]>1):
            self.dict[key] -=1
        else:
            del self.dict[key]
        return None
    def getMaxKey(self) -> str:
        if (self.check == 1):
            return self.result
        self.check = 1
        if (self.dict):
            maxv = list(self.dict.values())[0]
            maxk = list(self.dict.keys())[0]
            for i in self.dict.keys():
                if (self.dict[i]>maxv):
                    maxv = self.dict[i]
                    maxk = i
            self.result = maxk
            return maxk
        self.result = ""
        return ""
    def getMinKey(self) -> str:
        if (self.check == 2):
            return self.result
        self.check = 2
        if (self.dict):
            minv = list(self.dict.values())[0]
            mink = list(self.dict.keys())[0]
            for i in self.dict.keys():
                if (self.dict[i]<minv):
                    minv = self.dict[i]
                    mink = i
            self.result = mink
            return mink
        self.result = ""
        return ""
