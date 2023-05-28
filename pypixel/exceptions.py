"""
Custom exceptions for PyPixel
"""


class PyPixelException(Exception):
    """Base class for all PyPixel exceptions"""


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
    """Invalid secrets file provided"""

    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"Model {self.model} is not implemented yet"


class InvalidModelException(PyPixelException):
    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"{self.model} is not a valid model"


class CohereException(PyPixelException):
    """Invalid secrets file provided"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"Cohere Exception: {self.message}"


class DangerousCodeException(PyPixelException):
    """Invalid secrets file provided"""

    def __init__(self, code: str, keywords: list):
        self.code = code
        self.keywords = keywords

    def __str__(self):
        return f"Code has blacklisted keywords: {self.keywords} Code: {self.code}"
