class ClassA:
    def __init__(self, a, b, c):
        self.a = a          # public attribute
        self._b = b         # protected attribute
        self.__c = c        # private attribute
        
    def method_a(self):      # public method
        print("method_a =", self.a);
        
    def _method_b(self):     # protected method
        print("method_b =", self._b);
        
    def __method_c(self):    # private method
        print("method_c =", self.__c);
        
class ClassB(ClassA):
    def __init__(self, a, b, c, d):
        ClassA.__init__(self, a, b, c)
        self._d = d         # protected attribute
        
    def method_d(self):      # protected method
        print("method_d =", self._d);
        
    def method_test(self):   # protected method
        # These two attrobute are allowed
        print("a =", self.a)
        print("b =", self._b)        
        print("c =", self.__c)
        
        # these two method calls are allowed
        ClassA.method_a(self)
        ClassA._method_b(self)
        ClassA.__method_c(self)
        
def main():
    bobj = ClassB(2, 4, 6, 8)
    bobj.method_test()
    
    print("bobj.a =", bobj.a)
    print("bobj._b =", bobj._b)
    print("bobj.__c =", bobj.__c)
    
    bobj.method_a()
    bobj._method_b()
    bobj.__method_c()
    bobj.method_d()
if __name__ == "__main__":
    main()