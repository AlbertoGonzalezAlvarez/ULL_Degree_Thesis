from Genetic.Operations.Mutation import Mutation

class Simple_GA:

    def __init__(self, train_data: dict, test_data: dict, mutation_rate: int, initialPopulationSize: int):
        self.train_data = train_data
        self.test_data = test_data
        self.initialPopulationSize = initialPopulationSize
        self.population = []

        if mutation_rate > 0.0 and mutation_rate <= 1.0:
            Mutation.MUTATION_RATE = mutation_rate
        else:
            raise AttributeError("Mutation rate should be between (0.0 - 1.0]")

        for _ in range(initialPopulationSize):
            for category in test_data:
                print(len(category))
