import openai

from .base import Model


class OpenAI(Model):
    engine = "text-davinci-003"
    max_tokens = 1200
    temperature = 0
    top_p = 1
    frequency_penalty = 0.25
    presence_penalty = 0

    @property
    def model(self):
        return "OpenAI"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        openai.api_key = self._secrets.get("openai_api_key")

    def run(self, prompt):
        response = None
        try:
            response = openai.Completion.create(
                engine=self.engine,
                prompt=str(prompt),
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            )
        except openai.error.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            return
        except openai.error.APIConnectionError as e:
            print(f"Failed to connect to OpenAI API: {e}")
            return
        except openai.error.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
            return
        except openai.error.AuthenticationError as e:
            print(f"OpenAI API key is invalid: {e}")
            return

        return dict(response).get("choices")[0].get("text").strip()
