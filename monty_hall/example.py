class Priv:
    def __init__(self):
        self.public = 1
        self._protected = 2
        self.__private = 3  # _<class name><attribute name>


p = Priv()
print(p.public)
print(p._protected)
# attribute mangling
print(p._Priv__private)
