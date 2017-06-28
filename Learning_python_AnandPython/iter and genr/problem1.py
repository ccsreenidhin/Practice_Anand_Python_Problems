#Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::


class reviter:

    def __init__(self, n):
        self.n = len(n)
        self.i = len(n)

    def __iter__(self):
        return self


    def next(self):
        if self.i>0:
            i=self.i
            self.i-=1
            return i
        else:
            raise StopIteration()





it = reviter([1, 2, 3, 4])
print it

print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
