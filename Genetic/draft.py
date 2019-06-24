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

    def __hash__(self):
        return hash(self.vect)

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

print(vector.index(test("asdas", 9)))
vector.pop(vector.index(c))
# a = set([element.content for element in vector])
#
# vector = Vector(vector)
# print(vector)
print(sorted(vector))
vector.pop()
# asd = {"a": 2, "b": 4, "c": 3}
#
# print(list(asd.values()))
#
# #TODO: poblacion en el algoritmo genetico como un vector, no representarlo con una clase
#
#
# # from Genetic.Individual import *
# # from Genetic.PopulationUpdaters.Updaters import *
# #
# # #deprecated
# # class BasePopulation:
# #
# #     POPULATION_UPDATE_METHOD: type = None
# #
# #     def __init__(self, population: [BaseIndividual]):
# #         self.population: [BaseIndividual] = population
# #
# #     def update_population(self):
# #         BasePopulation.POPULATION_UPDATE_METHOD.update(self.actual_population, self.next_population)
#
# # class Test:
# #     test_types = {}
# #
# #     def __init_subclass__(cls):
# #         Test.test_types.update({cls.__name__: cls})
# #
# #     def __init__(self, value: int):
# #         self.value = value
# #
# #     def method(self, clas):
# #         print(clas.vect)
# #
# # asd = Test(1)
# # asd.method(Vector)
#
# # from sklearn.feature_extraction.text import TfidfVectorizer
# #
# #
# # vectorizer = TfidfVectorizer()
# # result = vectorizer.fit_transform(data_category.documents)
# # feature_names = vectorizer.get_feature_names()
# #
# # feature_tfidf_map = {}
# #
# # for index in set(result.nonzero()[1]):
# #     if result[0, index] > 0.0:
# #         feature_tfidf_map[feature_names[index]] = result[0, index]
# #
# # TFIDF.__TFIDF_VALUES__[data_category.name] = feature_tfidf_map
# #
# # class Vector:
# #     def __init__(self):
# #         self.vect = []
# #         self.current = 0
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         if self.current > len(self.vect) - 1:
# #             raise StopIteration
# #
# #         self.current += 1
# #         return self.vect[self.current - 1]
# #
# #     def __repr__(self):
# #         return str(self.vect)
# #
# class Test():
#
#     def __init__(self, vect1, vect2):
#         self.vect1 = vect1
#         self.vect2 = vect2
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         vector = self.vect1 + self.vect2
#
#         if self.current > len(vector) - 1:
#             raise StopIteration
#
#         self.current += 1
#
#         return vector[self.current - 1]
#
#     def __eq__(self, other):
#         return self.value == other.value
#
#
# # a = Test([9, 3, 354, 65, 54, 23, 9], [38, 93, 12, 39, 49, 12])
# #
# # for item in a:
# #     print(item)
# # a = Test()
# # b = Vector()
# #
# # print(isinstance(b, Test))
#
#
# # class WordGen:
# #     def __init__(self, cat, word):
# #         self.cat = cat
# #         self.word = word
# #
# #     def __repr__(self):
# #         return str(self.cat) + ": " + str(self.word)
# #
# #
# # list = [WordGen("crime", "dead"), WordGen("crime", "victim"), WordGen("gun", "police"),
# #         WordGen("gun", "steal"), WordGen("god", "coran"), WordGen("god", "bible")]
# #
# # newlist = sorted(list, key=lambda x: (x.cat, x.word), reverse=True)
# # print({word.cat for word in newlist})
#
# # class BaseIndividual():
# #     def __init__(self, chromosome):
# #         self.chromosome: set = set(chromosome)
# #         self.score: float = 0.0
# #
# #     def __lt__(self, other):
# #         return self.score < other.score
# #
# #     def __gt__(self, other):
# #         return self.score > other.score
# #
# #
# # class CategorizedIndividual(BaseIndividual):
# #     def __init__(self, chromosome: list):
# #         super().__init__(chromosome)
# #         self.chromosome: list = chromosome
# #
# # a = CategorizedIndividual([2,3, 4, 4])
# # print(a.score, a.chromosome)
#
# # from sklearn.datasets import fetch_20newsgroups
# # from sklearn.feature_extraction.text import CountVectorizer
# # from sklearn.feature_extraction.text import TfidfTransformer
# # from sklearn.naive_bayes import MultinomialNB
# # from sklearn.pipeline import Pipeline
# # from sklearn.metrics import f1_score
# #
# # text_clf = Pipeline([
# #     ('vect', CountVectorizer()),
# #     ('tfidf', TfidfTransformer()),
# #     ('clf', MultinomialNB()),
# # ])
# #
# # text_clf.fit(['asd', 'vcxzcx'], ['cat1', 'cat2'])
# # predicted = text_clf.predict(['asd', 'vcxzcx'])
# #
# # score_for_category = f1_score(['cat1', 'cat2'], predicted, average=None)
# #
# # print(sum(score_for_category))
#
# import numpy as np
# dic = {"a": 12, "b": 20, "c": 20}
# dic2 = {"a": 12, "b": 1, "c": 20}
#
# print(list(dic.values()), type(list(dic.values())))
# a = np.abs(np.sum(np.array(list(dic.values())) - np.array(list(dic2.values()))))
#
# print(a)