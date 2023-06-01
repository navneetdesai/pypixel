"""
Base class for all models
"""
import json
import os
from abc import ABC, abstractmethod

from dotenv import dotenv_values

import pypixel.constants as constants
from pypixel import UnimplementedModelException


class Model(ABC):
    prompt = None

    def __init__(self, **kwargs):
        """
        Initialize a model with the given kwargs (custom attributes)
        :param kwargs: custom attributes
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        if not hasattr(self, "_secrets"):
            self._secrets = self.read_secrets(constants.SECRETS)

    def __repr__(self):
        """
        String representation of the model
        :return: string representation of the model
        """
        return self.__str__()

    def __str__(self):
        """
        String representation of the model
        :return:  string representation of the model
        """
        return f"{self.__class__.__name__}"

    @property
    def model(self):
        """
        Return the model
        :return: the model
        """
        raise UnimplementedModelException(str(self))

    @abstractmethod
    def run(self, prompt):
        """
        Run the model on the given prompt
        :param prompt: prompt to run the model on
        :return:
        """
        raise UnimplementedModelException(str(self))

    @staticmethod
    def read_secrets(secrets_file: str) -> dict:
        """
        Read the secrets file and return the secrets
        :param secrets_file:
        :return:
        """
        if env_vars := dotenv_values("../../.env"):
            return env_vars
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            secrets_file = os.path.join(current_dir, secrets_file)
            with open(secrets_file) as f:
                return json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Secrets file {secrets_file} not found") from e
