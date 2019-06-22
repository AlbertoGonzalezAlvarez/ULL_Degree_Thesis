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

asd = {"a": 2, "b": 4, "c": 3}

print(list(asd.values()))

#TODO: poblacion en el algoritmo genetico como un vector, no representarlo con una clase


# from Genetic.Individual import *
# from Genetic.PopulationUpdaters.Updaters import *
#
# #deprecated
# class BasePopulation:
#
#     POPULATION_UPDATE_METHOD: type = None
#
#     def __init__(self, population: [BaseIndividual]):
#         self.population: [BaseIndividual] = population
#
#     def update_population(self):
#         BasePopulation.POPULATION_UPDATE_METHOD.update(self.actual_population, self.next_population)

# class Test:
#     test_types = {}
#
#     def __init_subclass__(cls):
#         Test.test_types.update({cls.__name__: cls})
#
#     def __init__(self, value: int):
#         self.value = value
#
#     def method(self, clas):
#         print(clas.vect)
#
# asd = Test(1)
# asd.method(Vector)

# from sklearn.feature_extraction.text import TfidfVectorizer
#
#
# vectorizer = TfidfVectorizer()
# result = vectorizer.fit_transform(data_category.documents)
# feature_names = vectorizer.get_feature_names()
#
# feature_tfidf_map = {}
#
# for index in set(result.nonzero()[1]):
#     if result[0, index] > 0.0:
#         feature_tfidf_map[feature_names[index]] = result[0, index]
#
# TFIDF.__TFIDF_VALUES__[data_category.name] = feature_tfidf_map

class Vector:
    def __init__(self):
        self.vect = []
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

class Test(Vector):

    def __init__(self):
        pass
        # self.value = Vector(vector)

    def __iter__(self):
        return self.value

a = Test()
b = Vector()

print(isinstance(b, Test))


d = {'x': 2}

d.update({"a": d["a"] + 5})
print(d)