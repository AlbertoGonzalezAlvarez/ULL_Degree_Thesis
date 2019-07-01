from __future__ import annotations
from EmailParser import Email
from Log import LoggerHandler

class DataCategory():

    def __init__(self, category_name: str = "", emails_data: list = []):
        self.name: str = category_name
        self.corpus: list[str] = []
        self.documents: list[str] = []

        for email in emails_data:
            self.corpus += (email.words_vector)
            self.documents.append(email.content)

        # Avoid repeated words
        self.corpus = list(set(self.corpus))
        self.lenght: int = len(self.corpus)

    def __len__(self):
        return self.lenght

    def documents_len(self):
        return len(self.documents)

    def getWorsdAt(self, indexs) -> str:
        if isinstance(indexs, int):
            return self.corpus[indexs]

        elif isinstance(indexs, list):
            return [self.corpus[index] for index in indexs]

        else:
            LoggerHandler.error(__name__, "You trying get an invalid word index")

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

