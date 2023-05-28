import ast

import pyflakes

from .constants import BLACKLIST, END, SECRETS, START
from .exceptions import *
from .models import Cohere, Model, OpenAI
from .prompts import GenerateCodePrompt, Prompt


class PyPixel:
    def __init__(self, model):
        self.model = model

    def __call__(self, prompt: str, **kwargs) -> str:
        code = self.generate_code(GenerateCodePrompt(prompt), self.model)

        if kwargs.get("write_to_file"):
            self.write_to_file(code, kwargs.get("write_to_file"))
        return code

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "PyPixel"

    def generate_code(self, prompt: Prompt, model: Model) -> str:
        if not isinstance(model, Model):
            raise InvalidModelException(str(model))

        if not isinstance(prompt, Prompt):
            raise InvalidPromptException(str(prompt))

        response = model.run(prompt)
        code = self.extract_code(response)
        if messages := self.check_code(code):
            print(f"Warning: {messages}")
        return code

    @staticmethod
    def extract_code(text):
        if START not in text or END not in text:
            raise InvalidCodeException(text)

        if words := [word for word in BLACKLIST if word in text]:
            raise DangerousCodeException(text, words)
        return text.split(START)[1].split(END)[0]

    @staticmethod
    def write_to_file(code, file_name):
        with open(file_name, "w") as f:
            f.write(code)

    @staticmethod
    def check_code(code):
        messages = []
        tree = compile(code, "generated_code", "exec", ast.PyCF_ONLY_AST)
        checker = pyflakes.Checker(tree, "generated_code")
        for warning in checker.messages:
            message = f"{warning.__class__.__name__}: {warning.message % warning.message_args}"

            messages.append(message)
        return messages
