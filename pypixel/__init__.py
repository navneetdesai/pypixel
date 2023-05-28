import json
import secrets

import cohere
from constants import END, SECRETS, START
from prompts import GenerateCodePrompt, Prompt


class PyPixel:
    def __init__(self):
        self.client = cohere.Client(self.read_secrets(SECRETS))

    def __call__(self, prompt: str) -> str:
        return self.generate_code(GenerateCodePrompt(prompt))

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def generate_code(self, prompt: Prompt) -> str:
        client = self.client
        response = client.generate(
            model="command",
            prompt=str(prompt),
            max_tokens=500,
            temperature=0.2,
            k=0,
            stop_sequences=[],
            return_likelihoods="NONE",
        )
        return self.extract_code(response.generations[0].text)

    @staticmethod
    def read_secrets(secrets_file: str) -> str:
        try:
            with open(secrets_file) as f:
                return json.load(f)["cohere_api_key"]
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Secrets file {secrets_file} not found") from e

    def extract_code(self, text):
        if START not in text or END not in text:
            raise ValueError(f"Invalid code generated: {text}")
        return text.split(START)[1].split(END)[0]
