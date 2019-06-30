_creator = "Tayler Uva"
_dash = "============================="


def _printKey(msg, fileName):
    from os.path import basename
    print(_dash,
          msg, "- %s" % basename(fileName),
          "- Created by %s" % _creator,
          _dash)


def hello(fileName, clear=True):  # Adds a default value for clear if one is not passed
    # Documentation Formatting
    """
    Clears the console and adds a header message.
    """
    if clear:
        _clearConsole()

    _printKey("START", fileName)
    print()


def goodbye(fileName):
    # Documentation Formatting
    """
    Adds footer message
    """
    print()
    _printKey("END", fileName)


def _clearConsole():
    # Documentation Formatting
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    from platform import system
    command = "cls" if system().lower() == "windows" else "clear"

    # Action
    from subprocess import call
    return call(command) == 0
