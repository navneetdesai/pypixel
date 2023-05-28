import json
import os

import pypixel.constants as constants


class Model:
    prompt = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.secrets = self.read_secrets(constants.SECRETS)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.__class__.__name__}"

    def run(self, prompt):
        raise NotImplementedError

    @staticmethod
    def read_secrets(secrets_file: str) -> str:
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            secrets_file = os.path.join(current_dir, secrets_file)
            with open(secrets_file) as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Secrets file {secrets_file} not found") from e
