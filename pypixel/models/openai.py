import logging

import openai

from ..exceptions import InvalidAttributeException, InvalidPromptException
from ..prompts import EditImagePrompt, GenerateImagePrompt
from .base import Model


class OpenAI(Model):
    engine = "text-davinci-003"
    max_tokens = 1200
    temperature = 0
    top_p = 1
    frequency_penalty = 0.25
    presence_penalty = 0

    _valid_sizes = "256x256", "512x512", "1024x1024"
    _images_per_request = range(1, 11)

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

    def generate_image(
        self, prompt: GenerateImagePrompt = None, size=None, num_images=None
    ):
        if not prompt or not isinstance(prompt, GenerateImagePrompt):
            raise InvalidPromptException(str(prompt))

        size, num_images = self.check_attributes(num_images, size)
        try:
            response = openai.Image.create(prompt=str(prompt), n=num_images, size=size)
        except openai.error.OpenAIError as e:
            print(f"OpenAI API returned an error: {e}")
            return
        return response.get("data")[0].get("url")

    def edit_image(
        self, image, mask, prompt: EditImagePrompt = None, num_images=None, size=None
    ):
        if not prompt or not isinstance(prompt, EditImagePrompt):
            raise InvalidPromptException(str(prompt))

        size, num_images = self.check_attributes(num_images, size)
        try:
            response = openai.Image.create_edit(
                image=image, mask=mask, prompt=str(prompt), n=num_images, size=size
            )
        except openai.error.OpenAIError as e:
            print(f"OpenAI API returned an error: {e}")
            return

        return response["data"][0]["url"]

    def check_attributes(self, num_images, size):
        if not size:
            size = self._valid_sizes[0]
            logging.warning("No size specified. Defaulting to 256x256")
        if not num_images:
            num_images = self._images_per_request[0]
            logging.warning("No number of images specified. Defaulting to 1")
        if size not in self._valid_sizes:
            raise InvalidAttributeException(f"Sizes supported. {self._valid_sizes}")
        if num_images not in self._images_per_request:
            raise InvalidAttributeException(
                f"Number of images supported: {self._images_per_request}"
            )

        return size, num_images
