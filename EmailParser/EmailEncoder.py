import json
from EmailParser.Email import Email

class EmailEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, Email):
            return  {
                            "category": object.category,
                            "from": object.from_,
                            "subject": object.subject,
                            "organization": object.organization,
                            "content": object.content
                    }
        else:
            return json.JSONEncoder.default(self, object)

    @staticmethod
    def encodeEmail(email):
        if 'category' in email:
            return Email(category=email["category"], from_=email['from'], subject=email['subject'],
                         organization=email['organization'], content=email['content'])
        return email
