class test:
    def __init__(self, content, value):
        self.content = content
        self.value = value

    def __hash__(self):
        return hash(self.content) + hash(self.value)

    def __eq__(self, other):
        return self.content == other.content and self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return str(self.content) + ": " + str(self.value)

class Vector:
    def __init__(self, vect):
        self.vect = vect
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > len(self.vect) - 1:
            raise StopIteration

        self.current += 1
        return self.vect[self.current - 1]

    def __repr__(self):
        return str(self.vect)

a = test("asd", 1)
z = test("asd", 1)
b = test("bcsd", 7)
c = test("asdas", 9)
e = test("asdas", 4)

vector = [a, b, c, z, e]

a = set([element.content for element in vector])

vector = Vector(vector)
print(vector)
print(sorted(vector))
