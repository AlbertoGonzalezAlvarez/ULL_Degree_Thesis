import GlobalConfig
import re
import json
from Utilities.WordCleaner import cleanWord

class Email:
    HEADER_LENGHT = 10

    def __init__(self, category: str, message: str) -> None:
        header = "".join(message.splitlines(Email.HEADER_LENGHT)[:Email.HEADER_LENGHT])
        organization = re.search(GlobalConfig.ORGANIZATION_REGEX, header)
        emailAdress = re.search(GlobalConfig.FROM_EMAIL_REGEX, header)

        # Maybe we could delete
        self.category = category
        self.subject = cleanWord(re.search(GlobalConfig.SUBJECT_REGEX, header).group(1).lower())
        self.content = cleanWord(message.replace(header, ''))

        if organization:
            self.organization = organization.group(1)
        else:
            self.organization = ""

        if emailAdress:
            self.emailAdress = emailAdress.group(1).lower()
        else:
            self.emailAdress = ""

    def __str__(self) -> str:
        JSON = {}
        JSON['category'] = f'{self.category}'
        JSON['from'] = f'{self.emailAdress}'
        JSON['subject'] = f'{self.subject}'
        JSON['organization'] = f'{self.organization}'
        JSON['content'] = f'{self.content}'

        return json.dumps(JSON, indent = 5)

    def __repr__(self) -> str:
        JSON = {}
        JSON['category'] = f'{self.category}'
        JSON['from'] = f'{self.emailAdress}'
        JSON['subject'] = f'{self.subject}'
        JSON['organization'] = f'{self.organization}'
        JSON['content'] = f'{self.content}'

        return json.dumps(JSON, indent = 5)