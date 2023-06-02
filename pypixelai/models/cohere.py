"""
Cohere API model.
"""


import cohere

from ..constants import COHERE_API_KEY
from .base import Model


class Cohere(Model):
    engine = "command"
    max_tokens = 1200
    temperature = 0.2
    k = 0
    stop_sequences = []
    return_likelihoods = "NONE"

    @property
    def model(self):
        """
        Returns the model name.
        :return: str
        """
        return "Cohere"

    def __init__(self, **kwargs):
        """
        Initialize the Cohere model.
        :param kwargs: dict
        """
        super().__init__(**kwargs)
        self.client = cohere.Client(self._secrets.get(COHERE_API_KEY))

    def run(self, prompt):
        """
        Run the model.
        :param prompt:
        :return:
        """
        response = self.client.generate(
            model=self.engine,
            prompt=str(prompt),
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            k=self.k,
            stop_sequences=self.stop_sequences,
            return_likelihoods=self.return_likelihoods,
        )
        return dict(response).get("generations")[0].get("text")
