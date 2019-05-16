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

    def __init__(self, category_name: str = "", data: [] = []):
        self.categoryName = category_name
        self.data = data
        self.lenght = sum(document.lenght for document in data)
        self.corpus = []

        for document in data:
            self.corpus += (document.words_vector)

        # DataCategories.EMAIL_CATEGORIES[category_name] = self

    @staticmethod
    def addTrainCategory(category_name: str = "", json_data: [] = [], fields: [] = []) -> None:
        emails = []

        for json_email in json_data:
            emails.append(Email.from_json(json_email, fields))

        LoggerHandler.log(__name__, f"Added new category to train '{category_name}'.")
        return DataCategories(category_name, emails)

    @staticmethod
    def addTestCategory(category_name: str = "", json_data: [] = [], fields: [] = []) -> None:
        emails = []

        for json_email in json_data:
            emails.append(Email.from_json(json_email, fields))

        LoggerHandler.log(__name__, f"Added new category to validate '{category_name}'.")
        return DataCategories(category_name, emails)

    def __str__(self):
        return self.categoryName + '\n' + str(self.data)


