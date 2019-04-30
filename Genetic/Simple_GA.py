from Genetic.Operations.Mutation import Mutation

class Simple_GA:

    population = []
    train_data = dict
    test_data = dict

    def __init__(self, train_data: dict, test_data: dict, mutation_rate: int):
        self.train_data = train_data
        self.test_data = test_data

        if mutation_rate > 0.0 and mutation_rate <= 1.0:
            Mutation.MUTATION_RATE = mutation_rate
        else:
            raise AttributeError("Mutation rate should be between (0.0 - 1.0]")


    def __init_population(self) -> None:
        pass