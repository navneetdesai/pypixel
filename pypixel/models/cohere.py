import cohere

from .base import Model


class Cohere(Model):
    model = "command"
    max_tokens = 1200
    temperature = 0.2
    k = 0
    stop_sequences = []
    return_likelihoods = "NONE"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = cohere.Client(self.secrets.get("cohere_api_key"))

    def run(self, prompt):
        response = self.client.generate(
            model=self.model,
            prompt=str(prompt),
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            k=self.k,
            stop_sequences=self.stop_sequences,
            return_likelihoods=self.return_likelihoods,
        )
        return response.generations[0].text
