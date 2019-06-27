import os
import json
from Log import LoggerHandler

class FileUtilities:

    DEFAULT_DIR = os.path.dirname(os.path.dirname(__file__)) + '\Data'
    FILE_REGISTER = []

    @staticmethod
    def startService():
        LoggerHandler.log(__name__, f"Fetching data from '{FileUtilities.DEFAULT_DIR}'")
        for file in os.listdir(FileUtilities.DEFAULT_DIR):
            FileUtilities.FILE_REGISTER.append(file)

    @staticmethod
    def writeToFile(content: object, fileName: str, directory: str = DEFAULT_DIR, encoder = json.JSONEncoder) -> None:
        fileName = os.path.join(directory, fileName)
        FileUtilities.FILE_REGISTER.append(fileName)
        LoggerHandler.log(__name__, f"Writing data to '{fileName}'")

        with open(fileName, "w+") as write_file:
            json.dump(content, write_file, cls = encoder, indent = 5)

    @staticmethod
    def readJSON(fileName: str, encoder: object = dict) -> object:
        fileName = os.path.join(FileUtilities.DEFAULT_DIR, fileName)
        LoggerHandler.log(__name__, f"Reading JSON file from '{fileName}'")

        with open(fileName) as json_file:
            content = json.load(json_file, object_hook = encoder)

        return content

    @staticmethod
    def isRegistred(*files) -> bool:
        for file in files:
            if str(file) not in FileUtilities.FILE_REGISTER:
                return False
        return True
