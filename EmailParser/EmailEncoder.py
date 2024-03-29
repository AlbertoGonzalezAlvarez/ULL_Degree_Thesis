import json
from EmailParser import Email

class EmailEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, Email):
            object = object.email_content
            return  {
                            "category": object['category'],
                            "from_": object['from_'],
                            "subject": object['subject'],
                            "organization": object['organization'],
                            "msg": object['msg']
                    }
        else:
            return json.JSONEncoder.default(self, object)

    @staticmethod
    def encodeEmail(email):
        if 'category' in email:
            return Email(email["category"], email['from_'], email['subject'], email['organization'], email['msg'])
        return email

    @staticmethod
    def getCorpusFromDict(data: dict) -> dict:
        corpus = {}
        for category in data:
            corpus[category] = [Email(**Email.parseEmail(category, email)) for email in data[category]]

        return corpus