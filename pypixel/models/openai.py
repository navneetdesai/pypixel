import openai

from .base import Model


class OpenAI(Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        openai.api_key = self.secrets.get("openai_api_key")

    def run(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=str(prompt),
            max_tokens=1200,
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].text.strip()
