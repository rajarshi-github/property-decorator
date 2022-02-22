

class c1:
    def __init__(self, a = 10, b = 20 , c = 30):
        self.a = a
        self.b = b
        self.c = c

    @property
    def aggr(self):
        return f"{self.a + self.b + self.c:.2f}"

    @aggr.setter
    def aggr(self, val):
        self.a = val*1
        self.b = val*2
        self.c = val*3

    @aggr.deleter
    def aggr(self):
        del self.a
        del self.b
        del self.c

if __name__ == '__main__':
    obj1 = c1()

    print('You can use `aggr` just as if it were an attribute')
    print(f"{obj1.aggr=}")
    print('But if you check the dictionary of the `obj` there is no `aggr`')
    print(f"{obj1.__dict__=}")
    print('Hence understand once again that its nothing but a function which returns another function, i.e decorator')
    print(f"{obj1.a=}, {obj1.b=}, {obj1.c=}")
