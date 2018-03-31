from django.core.exceptions import ValidationError



def validate_content(value):
    content = value
    if content == "a":
        raise ValidationError("Content Cannot be empty")
    return value
