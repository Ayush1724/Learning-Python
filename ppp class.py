class abc:
    a=20
    _a=30
    __a=40
    def show(self):
        print(self.a)
    def showw(self):
        print(self.__a)
    def showww(self):
        print(self._a)
class abcd(abc):
        pass    
obj=abc()
obj.a=12
obj.show