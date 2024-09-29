import re
from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneSymbol(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net", "uk")
MIN_SYMBOLS_COUNT = 4
email_pattern = r'^[a-zA-Z0-9._-]+@[a-z0-9]+[.][a-z.]{2,6}$'
pattern = r'\w+'

email = input()
while email != "End":

    if not re.match(email_pattern, email):
        if email.count("@") > 1:
            raise MoreThanOneSymbol("Email should contain only one @ symbol!")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @ !")
        if len(email.split("@")[0]) <= MIN_SYMBOLS_COUNT:
            raise NameTooShortError("Name must be more than 4 characters")
        if email.split(".")[-1] not in VALID_DOMAINS:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join("." + d for d in VALID_DOMAINS)}")
        if re.findall(pattern, email.split('@')[0])[0] != email.split("@")[0]:
            raise InvalidDomainError("Name must contain only letters, digits and underscores!")
    else:

        print("Email is valid")

    email = input()



