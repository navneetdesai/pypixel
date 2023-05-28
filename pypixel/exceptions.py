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
