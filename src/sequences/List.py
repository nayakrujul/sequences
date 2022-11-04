class List(list):
    def push(self, item):
        self.insert(0, item)
    def _first(self, types, b=True, n=1):
        k = n
        ret = []
        for item in self:
            if isinstance(item, types) == b:
                k -= 1
                ret.append(item)
                if not k:
                    break
        return ret
    def first(self, types, b=True, n=1):
        f = self._first(types, b, n)
        while len(f) < n:
            if (types == str) or (isinstance(types, tuple) and (str in types)):
                i = input()
                f.insert(0, i)
                self.push(i)
            elif (types == list) or (isinstance(types, tuple) and (list in types)):
                i = input().split()
                f.insert(0, i)
                self.push(i)
            else:
                i = eval(input())
                f.insert(0, i)
                self.push(i)
        if n>1:
            return f
        return f[0]
    @property
    def sum(self):
        if not self:
            return 0
        return sum(self[1:], start=self[0])
    @property
    def product(self):
        ret = 1
        for item in self:
            ret *= item
        return ret
    def removeAll(self, item):
        while item in self:
            self.remove(item)
    @property
    def repeat(self):
        class RepeatingList(List):
            def __init__(self, lst):
                self.lst = lst
                super().__init__(lst)
            def __iter__(self):
                while True:
                    for i in self.lst:
                        yield i
        return RepeatingList(self)
        
