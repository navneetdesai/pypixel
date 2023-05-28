import json
import os
import secrets

import cohere

from .constants import END, SECRETS, START
from .exceptions import *
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

    def generate_code(self, prompt: Prompt) -> str:
        client = self.client
        response = client.generate(
            model="command",
            prompt=str(prompt),
            max_tokens=500,
            temperature=0.5,
            k=0,
            stop_sequences=[],
            return_likelihoods="NONE",
        )
        return self.extract_code(response.generations[0].text)

    @staticmethod
    def read_secrets(secrets_file: str) -> str:
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            secrets_file = os.path.join(current_dir, secrets_file)
            with open(secrets_file) as f:
                return json.load(f)["cohere_api_key"]
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Secrets file {secrets_file} not found") from e

    @staticmethod
    def extract_code(text):
        if START not in text or END not in text:
            raise InvalidCodeException(text)
        return text.split(START)[1].split(END)[0]

    @staticmethod
    def write_to_file(code, file_name):
        with open(file_name, "w") as f:
            f.write(code)
