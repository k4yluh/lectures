# To define a new type, "Pair":
class Pair:
    """ A pair of elements """

    # Whenever a value is created of type Pair, its first and second
    #  attributes must be specified.
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # Two values of type Pair are equal if and only if they contain the same
    #  elements in the same order.
    def __eq__(self, other):
        return (type(self) == type(other)
                and self.first == other.first
                and self.second == other.second)

    # As a general rule of thumb, stringifying a value should provide enough
    #  information to recreate that value:
    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.second)
