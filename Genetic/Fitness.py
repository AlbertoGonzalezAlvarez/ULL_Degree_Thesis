from Log.LoggerHandler import LoggerHandler
from sklearn.feature_extraction.text import TfidfVectorizer

class Fitness():

    def __init__(self, geneticAlg: type):
        self.geneticAlg = geneticAlg
        self.tfidfFreq = {}

        for category in self.geneticAlg.train_data:
            self.tfidfFreq[category] = []

    @staticmethod
    def startUp(geneticAlg: type):
        from Genetic.Simple_GA import Simple_GA
        if (type == None or not isinstance(geneticAlg, Simple_GA)):
            LoggerHandler.error(__name__, "Fitness function must receive a genetic algorithm.")
        else:
            return Fitness(geneticAlg)

    # @staticmethod
    # def computeFitness(geneticAlg: type):
    #     if (type == None or not isinstance(geneticAlg, Simple_GA)):
    #         LoggerHandler.error(__name__, "Fitness function must receive a genetic algorithm.")



