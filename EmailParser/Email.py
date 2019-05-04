import json
import GlobalConfig
import re
from Utilities.WordCleaner import cleanWord
from Log.LoggerHandler import LoggerHandler

class Email(json.JSONEncoder):
    HEADER_LENGHT = 10

    def __init__(self, category: str ="", from_: str = "", subject: str = "", organization: str = "", content: str = "") -> None:
        self.category = category
        self.from_ = from_
        self.subject = subject
        self.organization = organization
        self.content = content

    @classmethod
    def from_json(cls, json_str):
        listOfEmails = {}

        if type(json_str) != dict:
            LoggerHandler.error(__name__, "You are trying to impor a JSON that isn't a dict")

        for category in json_str:
            if type(json_str[category]) == list:
                listOfEmails[category] = [cls(**email)for email in json_str[category]]

        return listOfEmails

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def parseEmail(category: str, content: str) -> object:
        header = "".join(content.splitlines(Email.HEADER_LENGHT)[:Email.HEADER_LENGHT])
        organization = re.search(GlobalConfig.ORGANIZATION_REGEX, header)
        emailAdress = re.search(GlobalConfig.FROM_EMAIL_REGEX, header)

        # Maybe we could delete
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
        JSON['category'] = f'{self.category}'
        JSON['from'] = f'{self.from_}'
        JSON['subject'] = f'{self.subject}'
        JSON['organization'] = f'{self.organization}'
        JSON['content'] = f'{self.content}'

        return json.dumps(JSON, indent = 5)

    def __repr__(self) -> str:
        JSON = {
            "email":
                {
                    "category": self.category,
                    "from": self.from_,
                    "subject": self.subject,
                    "organization": self.organization,
                    "content": self.content
                }
        }

        return json.dumps(JSON, indent = 5)