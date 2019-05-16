from EmailParser.Email import Email
from Log.LoggerHandler import LoggerHandler

class MetaEmailCategory(type):
    def __getitem__(self, index) -> None:
        if type(index) == str:
            return EmailCategory.EMAIL_CATEGORIES[index]
        else:
            return list(EmailCategory.EMAIL_CATEGORIES.values())[index]

class EmailCategory(metaclass = MetaEmailCategory):

    EMAIL_CATEGORIES = {}

    def __init__(self, category_name: str = "", data: [] = []):
        self.category_name = category_name
        self.data = data
        # self.lenght = len(emails_data)
        EmailCategory.EMAIL_CATEGORIES[category_name] = data

        LoggerHandler.log(__name__, f"Added new category '{self.category_name}'.")

    @property
    def name(self):
        return self.category_name

    @staticmethod
    def addCategory(category_name: str = "", json_data: [] = [], fields: [] = []) -> None:
        emails = []

        for json_email in json_data:
            emails.append(Email.from_json(json_email, fields))

        return EmailCategory(category_name, emails)

    def __str__(self):
        return self.category_name + '\n' + str(self.data)


