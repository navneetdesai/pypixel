import json
import os

import cohere
import openai

from .constants import END, SECRETS, START
from .exceptions import *
from .models import Cohere, Model, OpenAI
from .prompts import GenerateCodePrompt, Prompt


class PyPixel:
    def __init__(self):
        self.client = cohere.Client(self.read_secrets(SECRETS))

    def __call__(self, prompt: str, **kwargs) -> str:
        code = self.generate_code(GenerateCodePrompt(prompt))
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

        model.run(prompt)

    @staticmethod
    def extract_code(text):
        if START not in text or END not in text:
            raise InvalidCodeException(text)
        return text.split(START)[1].split(END)[0]

    @staticmethod
    def write_to_file(code, file_name):
        with open(file_name, "w") as f:
            f.write(code)
