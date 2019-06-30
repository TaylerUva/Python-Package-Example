
def get_password(service):
    from keyring import get_credential
    try:
        return get_credential(service, "").password
    except AttributeError:
        _set_password(service)
        return get_credential(service, "").password


def _set_password(service):
    from keyring import set_password
    from getpass import getpass
    set_password(service, input("Username: "), getpass.getpass())


def delete_password(service):
    from keyring import get_credential, delete_password
    delete_password(
        service,
        get_credential(service, "").username)
