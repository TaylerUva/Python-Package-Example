import keyring
import getpass
from keyring import credentials


def get_password(service):
    try:
        return keyring.get_credential(service, "").password
    except AttributeError:
        set_password(service)
        return keyring.get_credential(service, "").password


def set_password(service):
    keyring.set_password(service, input("Username: "), getpass.getpass())


def delete_password(service):
    keyring.delete_password(
        service,
        keyring.get_credential(service, "").username)
