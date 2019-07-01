import itertools
import json
import copy


class TestRunner:
                            # Ind_len        #Mutation       #Crossover      #Population
    POSIBLE_CONFIGS: list = [[0.3, 0.2],     [0.1, 0.05],      [0.8, 1.0],     [30, 50]]
    N_OF_EXECUTIONS: int = 10
    CONFIG_DIR: str = "Tests/Config.json"
    BASE_CONFIG: dict = {
        # To modify
        "crossover_prob": 0,
        "mutation_prob": 0,
        "individual_max_len": 0,
        "population_size": 0,
        # Fixed params
        "penalty_rate": 0.5,
        "max_generations": 150,
        "parents_offsprings": 2,
        "chromosome": "BaseChromosome",
        "gen": "BaseGen",
        "individual": "BaseIndividual",
        "population_updater": "BestsIndividuals",
        "parent_selector": "Tournament",
        "penalization_function": "PenaltyDistribution",
        "crossover": "UniformCrossover",
        "mutation": "ControlledMutation",
        "population_generator": "ApproximatedSize"
    }

    @classmethod
    def run_test(cls, test_id: int) -> tuple:
        with open(cls.CONFIG_DIR, 'r') as f:
            config_params = json.load(f)

        return (config_params["n_of_executions"], config_params["test_to_execute"][test_id]["test_description"])

    @classmethod
    def generate_config(cls) -> None:
        root_node: dict = {
            "n_of_executions": cls.N_OF_EXECUTIONS,
            "test_to_execute": []
        }

        config_combinations: list = list(itertools.product(*cls.POSIBLE_CONFIGS))
        test_index: int = 0

        for possible_config in config_combinations:
            config: dict = copy.deepcopy(cls.BASE_CONFIG)
            config["individual_max_len"] = possible_config[0]
            config["mutation_prob"] = possible_config[1]
            config["crossover_prob"] = possible_config[2]
            config["population_size"] = possible_config[3]

            root_node["test_to_execute"].append({
                "test_id": test_index,
                "test_description": config
            })

            test_index += 1

        file = open(cls.CONFIG_DIR, "w+")
        file.write(json.dumps(root_node, indent = 5))


