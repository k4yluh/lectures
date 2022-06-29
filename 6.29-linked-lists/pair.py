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
