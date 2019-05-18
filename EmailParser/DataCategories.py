from __future__ import annotations
from EmailParser.Email import Email
from Log.LoggerHandler import LoggerHandler

# class MetaDataCategories(type):
#     def __getitem__(self, index) -> None:
#         if type(index) == str:
#             return DataCategories.EMAIL_CATEGORIES[index]
#         else:
#             return list(DataCategories.EMAIL_CATEGORIES.values())[index]

class DataCategories():

    # EMAIL_CATEGORIES = {}

    def __init__(self, category_name: str = "", data: list = []):
        self.categoryName: str = category_name
        self.data: list = data
        self.lenght: int = sum(document.lenght for document in data)
        self.corpus: list = []

        for document in data:
            self.corpus += (document.words_vector)

        # DataCategories.EMAIL_CATEGORIES[category_name] = self

    @staticmethod
    def addTrainCategory(category_name: str = "", data_array: list = [], fields: list = []) -> DataCategories:
        emails = []

        for json_email in data_array:
            emails.append(Email.from_json(json_email, fields))

        LoggerHandler.log(__name__, f"Added new category to train '{category_name}'.")
        return DataCategories(category_name, emails)

    @staticmethod
    def addTestCategory(category_name: str = "", data_array: list = [], fields: list = []) -> DataCategories:
        emails = []

        for json_email in data_array:
            emails.append(Email.from_json(json_email, fields))

        LoggerHandler.log(__name__, f"Added new category to validate '{category_name}'.")
        return DataCategories(category_name, emails)

    @property
    def name(self) -> str:
        return self.categoryName

    def __str__(self):
        return self.categoryName + '\n' + str(self.data)


