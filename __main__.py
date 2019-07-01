from EmailParser import EmailEncoder, DataCategory
from Utilities import FileUtilities
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfTransformer
from Genetic import *
from sklearn.multiclass import *
from sklearn.svm import *
from sklearn.metrics import *
import time
from Tests.TestRunner import TestRunner
from os import system, path
import sys
import os
import json

## TESTS CONFIG
TEST_DIR = "./Data/"
TEST_PREFIX = "test_"
FILE_CONTENT: dict = {
    "genetic_algorithm_config": None,
    "final_classifier": {
        "categories": None,
        "f1_score": None,
        "recall": None,
        "precision": None
    },
    "elapsed_time": None,
    "evolution": None,
    "best_individual": None
}


if not path.exists(TestRunner.CONFIG_DIR):
    TestRunner.generate_config()

test_id: int =  int(sys.argv[1])
config: tuple = TestRunner.run_test(test_id)
execution_times, config_to_run = config[0], config[1]

config_name: str = f'crossover-{config_to_run["crossover_prob"]}_mutation-{config_to_run["mutation_prob"]}' \
    f'_individuallen-{config_to_run["individual_max_len"]}_populationlen-{config_to_run["population_size"]}'
system("title " + config_name)
TEST_DIR += config_name.lower()
os.mkdir(TEST_DIR)

if len(sys.argv) > 2 and bool(sys.argv[2]):
    graphic_mode: bool = True
else:
    graphic_mode: bool = False

train_data_dict = FileUtilities.readJSON("train_data.json")
test_data_dict = FileUtilities.readJSON("test_data.json")

train_data = [DataCategory.addTrainCategory(category, train_data_dict[category], ['from_', 'subject', 'msg']) for category in train_data_dict]
test_data = [DataCategory.addTestCategory(category, test_data_dict[category], ['from_', 'subject', 'msg']) for category in test_data_dict]

for execution_id  in range(execution_times):
    problem_spec: GeneticAlgorithmSpecification = GeneticAlgorithmSpecification(train_data, **config_to_run)
    genetic_algorithm: GeneticAlgorithm = GeneticAlgorithm(problem_spec, TEST_DIR, execution_id=execution_id)
    ELAPSED_TIME, RESULTS  = genetic_algorithm.start(time.time(), graphic_mode)
    best_solution: dict = genetic_algorithm.get_solution()

    train_documents = []
    train_labels: list = []
    test_labels = []
    test_documents = []

    for category in best_solution:
        train_labels += [category]

    for words in list(best_solution.values()):
        train_documents.append(" ".join(words))

    for category in test_data:
        test_labels += [category.name] * category.documents_len()

    for index in range(len(test_data)):
        test_documents += test_data[index].documents

    text_clf = Pipeline([
                ('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', OneVsRestClassifier(LinearSVC(class_weight="balanced")))
            ])

    text_clf.fit(train_documents, train_labels)
    predicted = text_clf.predict(test_documents)

    FILE_CONTENT['final_classifier']['categories'] = list(set(train_labels))
    FILE_CONTENT['final_classifier']['f1_score'] = list(f1_score(test_labels, predicted, average=None))
    FILE_CONTENT['final_classifier']['precision'] = list(precision_score(test_labels, predicted, average=None))
    FILE_CONTENT['final_classifier']['recall'] =  list(recall_score(test_labels, predicted, average=None))
    FILE_CONTENT['genetic_algorithm_config'] = config_to_run
    FILE_CONTENT['elapsed_time'] = ELAPSED_TIME
    FILE_CONTENT['evolution'] = RESULTS
    FILE_CONTENT['best_individual'] = best_solution

    file = open(TEST_DIR + '/' + TEST_PREFIX + str(execution_id) + ".json", "w+")
    file.write(json.dumps(FILE_CONTENT, indent = 5))

    print("================== CLASSIFICATION RESULTS ==================")
    print(classification_report(test_labels, predicted, target_names=train_labels))
