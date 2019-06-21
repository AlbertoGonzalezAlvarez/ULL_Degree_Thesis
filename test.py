# class ParentSelector():
#     method = {}
#
#     def __init_subclass__(cls):
#         ParentSelector.method.update({cls.__name__: cls})
#
#     @staticmethod
#     def selectParents(population, selectionMethod, parents=2):
#         list_of_parents = []
#
#         for _ in range(parents):
#             list_of_parents.append(selectionMethod.getParent(population))
#
#         return list_of_parents
#
# class RouletteWheel(ParentSelector):
#     @staticmethod
#     def getParent(population):
#         return population[0]
#
#
# # print(ParentSelector.SELECTION_METHODS)
# # print(ParentSelector.methods('RouletteWheel'))
# population = [3, 4, 49, 239, 234]
# print(ParentSelector.selectParents(population, ParentSelector.method['RouletteWheel']))

# class ReplacementMethods():
#     method = {}
#
#     def __init_subclass__(cls):
#         if 'desendancy' not in dir(cls):
#             raise ValueError(cls.__name__ + ' has no desendancy() method')
#
#         ReplacementMethods.method.update({cls.__name__: cls})
#
#     @staticmethod
#     def getDesendancy(replacementMethod, parents, offsprings):
#         return replacementMethod.desendancy(parents, offsprings)
#
# class BestIndividuals(ReplacementMethods):
#     @staticmethod
#     def desendancy(parents, offsprings):
#         return [parents[0], offsprings[0]]
#
#
# print(ReplacementMethods.getDesendancy(ReplacementMethods.method['BestIndividuals'], [1,2,3], [9,8,7]))

class test:
    def __init__(self, dct):
        self.dct = dct



dct = {
    "asd":
}