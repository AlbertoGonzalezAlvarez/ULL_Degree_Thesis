import os
import json
from EmailParser import EmailEncoder
from Log.LoggerHandler import LoggerHandler

class FileUtilities:

    DEFAULT_DIR = os.path.dirname(os.path.dirname(__file__)) + '\Data\\'
    FILE_REGISTER = []

    @staticmethod
    def writeToFile(content: object, filename: str, directory: str = DEFAULT_DIR, encoder = json.JSONEncoder ) -> None:
        fileDir = FileUtilities.DEFAULT_DIR + filename

        FileUtilities.FILE_REGISTER.append(fileDir)
        with open(fileDir, "w") as write_file:
            json.dump(content, write_file, cls = encoder, indent = 5)

    @staticmethod
    def readJSON(filename: str, encoder: object = dict) -> object:
        with open(FileUtilities.DEFAULT_DIR + filename) as json_file:
            content = json.load(json_file, object_hook = encoder)

        return content
