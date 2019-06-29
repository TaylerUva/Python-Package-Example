import time
import os
import subprocess
import platform
__creator = "Tayler Uva"
__dash = "============================="


def __printKey(msg, fileName):
    print(__dash,
          msg, "- %s" % os.path.basename(fileName),
          "- Created by %s" % __creator,
          __dash)


def hello(fileName, clear=True):  # Adds a default value for clear if one is not passed
    # Documentation Formatting
    """
    Clears the console and adds a header message.
    """
    if clear:
        __clearConsole()

    __printKey("START", fileName)
    print()


def goodbye(fileName):
    # Documentation Formatting
    """
    Adds footer message
    """
    print()
    __printKey("END", fileName)


def __clearConsole():
    # Documentation Formatting
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if platform.system().lower() == "windows" else "clear"

    # Action
    return subprocess.call(command) == 0
