class Pair:
    """ A pair of elements """

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        return (type(self) == type(other)
                and self.first == other.first
                and self.second == other.second)

    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.second)


# To represent a list of three elements using pairs that can only contain
#  two elements each:
lst = Pair('a', Pair('b', Pair('c', None)))
print(lst);

# To access the element at index 0 within this chain of pairs:
print(lst.first)

# To access the element at index 1 within this chain of pairs:
print(lst.second.first)

# To access the element at index 2 within this chain of pairs:
print(lst.second.second.first)
