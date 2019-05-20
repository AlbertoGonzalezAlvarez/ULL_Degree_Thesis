from __future__ import annotations
from EmailParser.Email import Email
from Log.LoggerHandler import LoggerHandler

class DataCategory():

    NUMBER_OF_CATEGORIES: int = 0

    def __init__(self, category_name: str = "", documents_data: list = []):
        self.categoryName: str = category_name
        # TODO: maybe we could delete this attribute
        self.data: list[Email] = documents_data
        self.lenght: int = sum(document.lenght for document in documents_data)
        self.document_words_vector: list[str] = []
        self.documents: list[str] = []

        for document in documents_data:
            self.document_words_vector += (document.words_vector)
            self.documents.append(document.corpus)

        DataCategory.NUMBER_OF_CATEGORIES += 1

    @property
    def corpus(self):
        return self.document_words_vector

    @staticmethod
    def addTrainCategory(category_name: str = "", data_array: list = [], fields: list = []) -> DataCategory:
        emails = []

        for json_email in data_array:
            emails.append(Email.from_json(json_email, fields))

        LoggerHandler.log(__name__, f"Added new category to train '{category_name}'.")
        return DataCategory(category_name, emails)

    @staticmethod
    def addTestCategory(category_name: str = "", data_array: list = [], fields: list = []) -> DataCategory:
        emails = []

        for json_email in data_array:
            emails.append(Email.from_json(json_email, fields))

        LoggerHandler.log(__name__, f"Added new category to validate '{category_name}'.")
        return DataCategory(category_name, emails)

    @property
    def name(self) -> str:
        return self.categoryName

    def __str__(self):
        return self.categoryName + '\n' + str(self.data)


