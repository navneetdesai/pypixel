"""
Custom exceptions for PyPixel
"""


class PyPixelException(Exception):
    """Base class for all PyPixel exceptions"""


class InvalidAttributeException(PyPixelException):
    """Invalid attribute provided"""

    def __init__(self, attribute: str):
        self.attribute = attribute

    def __str__(self):
        return f"Invalid attribute provided: {self.attribute}"


class InvalidCodeException(PyPixelException):
    """Invalid code generated"""

    def __init__(self, code: str):
        self.code = code

    def __str__(self):
        return f"Invalid code generated: {self.code}"


class InvalidPromptException(PyPixelException):
    """Invalid prompt provided"""

    def __init__(self, prompt: str):
        self.prompt = prompt

    def __str__(self):
        return f"Invalid prompt provided: {self.prompt}"


class InvalidSecretsException(PyPixelException):
    """Invalid secrets file provided"""

    def __init__(self, secrets_file: str):
        self.secrets_file = secrets_file

    def __str__(self):
        return f"Invalid secrets file provided: {self.secrets_file}"


class UnimplementedModelException(PyPixelException):
    """Model is not implemented yet"""

    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"Model {self.model} is not implemented yet"


class InvalidModelException(PyPixelException):
    """Model is not valid"""

    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"{self.model} is not a valid model"


class CohereException(PyPixelException):
    """Exceptions raised by the Cohere API"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"Cohere Exception: {self.message}"


class DangerousCodeException(PyPixelException):
    """Generated code has blacklisted keywords"""

    def __init__(self, code: str, keywords: list):
        self.code = code
        self.keywords = keywords

    def __str__(self):
        return f"Code has blacklisted keywords: {self.keywords} Code: {self.code}"
