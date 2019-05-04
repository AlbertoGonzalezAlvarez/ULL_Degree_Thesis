# from sklearn.model_selection import cross_val_score
# from sklearn.datasets import load_iris
# from sklearn.ensemble import AdaBoostClassifier
#
# iris = load_iris()
# clf = AdaBoostClassifier(n_estimators=100)
# scores = cross_val_score(clf, iris.data, iris.target, cv=5)
# print(scores)

class User(object):
    def __init__(self, name, username):
        self.name = name
        self.username = username

import json
def object_decoder(obj):
    if 'name' in obj:
        return User(obj['name'], obj['username'])
    return obj

a = json.loads('{"name": "John Smith", "username": "jsmith"}',
           object_hook=object_decoder)

print(type(a))  # -> <type 'type'>

print(a.name)