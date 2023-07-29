class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError
        self.size += n


    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError
        self.size -= n



    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        self._size = size


a = Jar(200)
print(a)
a.deposit(133)
print(a)
a.deposit(7)
print(a)
a.withdraw(5)
print(a)
