import os
from Log.LoggerHandler import LoggerHandler

class FileUtilities:

    DEFAULT_DIR = os.path.dirname(os.path.dirname(__file__)) + '\Data\\'
    FILE_REGISTER = []

    @staticmethod
    def writeToFile(content: object, filename: str, directory: str = DEFAULT_DIR) -> None:
        fileDir = FileUtilities.DEFAULT_DIR + filename

        FileUtilities.FILE_REGISTER.append(fileDir)
        file = open(fileDir, "w")
        file.write(str(content))
        file.close()

