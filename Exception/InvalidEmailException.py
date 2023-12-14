

class InvalidEmailFormatException(Exception):
    pass

    def validate_email(Email):
        if '@' not in Email or "." not in Email:
            raise InvalidEmailFormatException("Invalid Email format")