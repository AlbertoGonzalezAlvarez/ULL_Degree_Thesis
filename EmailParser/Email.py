import json
from EmailParser import GlobalConfig
import re
from Utilities import cleanWord
from Log import LoggerHandler

class Email(json.JSONEncoder):
    HEADER_LENGHT = 10
    DEFAULT_FIELDS = ['category', 'from_', 'subject', 'organization', 'content']

    def __init__(self, category: str ="", from_: str = "", subject: str = "", organization: str = "", content: str = "", fields: [] = DEFAULT_FIELDS) -> None:
        self.email_desired_fields = fields
        self.vector_of_words = []
        self.email_joined_fields = ""
        self.email_content = {
            'category': category,
            'from_': from_,
            'subject': subject,
            'organization': organization,
            'content': content
        }

    # Returns word at index position, taking in account all email fields
    def getWordAtAbsoluteIndex(self, index):
        self.__join_fields_data()
        return self.email_joined_fields[index]

    def __join_fields_data(self):
        if (len(self.email_joined_fields) <= 0):
            self.email_joined_fields = ""
            for field in self.email_desired_fields:
                self.email_joined_fields += self.email_content[field]

    @property
    def corpus(self):
        self.__join_fields_data()
        return self.email_joined_fields

    @property
    def lenght(self):
        self.words_vector
        return len(self.vector_of_words)

    @property
    def words_vector(self):
        if(len(self.vector_of_words) > 0):
            return self.vector_of_words

        self.__join_fields_data()
        self.vector_of_words = re.findall(r'\w+', self.email_joined_fields)
        return self.vector_of_words


    @classmethod
    def from_json(cls, email: str, fields: [] = DEFAULT_FIELDS) -> None:
        if type(email) != dict:
            LoggerHandler.error(__name__, "You are trying to import a JSON that isn't a dict")

        return Email(**email, fields = fields)

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def parseEmail(category: str, content: str) -> object:
        header = "".join(content.splitlines(Email.HEADER_LENGHT)[:Email.HEADER_LENGHT])
        organization = re.search(GlobalConfig.ORGANIZATION_REGEX, header)
        emailAdress = re.search(GlobalConfig.FROM_EMAIL_REGEX, header)

        category = category
        subject = cleanWord(re.search(GlobalConfig.SUBJECT_REGEX, header).group(1).lower())
        content = cleanWord(content.replace(header, ''))

        if organization:
            organization = organization.group(1)
        else:
            organization = ""

        if emailAdress:
            emailAdress = emailAdress.group(1).lower()
        else:
            emailAdress = ""

        return {
            "category": category,
            "from_": emailAdress,
            "subject": subject,
            "organization": organization,
            "content": content
        }

    def __str__(self) -> str:
        JSON = {}
        for desired_field in self.email_desired_fields:
            JSON[desired_field] = self.email_content[desired_field]

        return json.dumps(JSON, indent=5)

    def __repr__(self) -> str:
        JSON = {}
        for desired_field in self.email_desired_fields:
            JSON[desired_field] = self.email_content[desired_field]

        return json.dumps(JSON, indent = 5)