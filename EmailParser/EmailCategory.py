class EmailCategory:

    EMAIL_CATEGORIES = {}

    def __init__(self, category_name: str = "", emails_data: str = ""):
        # str
        self.category_name = category_name
        # str
        self.data = emails_data
        # int
        self.lenght = len(emails_data)
        EmailCategory.EMAIL_CATEGORIES[category_name] = category_name, emails_data

    @staticmethod
    def addCategory(category_name: str = "", emails_data: type = []) -> None:
        email_corpus = [email.content for email in emails_data]
