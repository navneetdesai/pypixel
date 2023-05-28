import openai

from .base import Model


class OpenAI(Model):
    engine = "text-davinci-003"
    max_tokens = 1200
    temperature = 0
    top_p = 1
    frequency_penalty = 0.25
    presence_penalty = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        openai.api_key = self.secrets.get("openai_api_key")

    def run(self, prompt):
        response = openai.Completion.create(
            engine=self.engine,
            prompt=str(prompt),
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
        return response.choices[0].text.strip()
