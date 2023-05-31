import ast
import logging
import os
from datetime import datetime

import pyflakes
import requests

from .constants import BLACKLIST, DOWNLOAD_DIR, END, SECRETS, START
from .exceptions import *
from .models import Cohere, Model, OpenAI
from .prompts import *


class PyPixel:
    debug: False
    retries = 1

    def __init__(self, model, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.model = model

    def __call__(self, prompt: str, **kwargs) -> str:
        code = self.generate_code(GenerateCodePrompt(prompt), self.model)
        self.retries -= 1
        if kwargs.get("write_to_file"):
            self.write_to_file(code, kwargs.get("write_to_file"))
        if kwargs.get("run_code"):
            try:
                if self.debug:
                    print(f"Running code: {code}")
                exec(code, globals(), locals())
            except Exception as e:
                if self.retries > 0:
                    self.generate_code(FixCodePrompt(prompt, code, e), self.model)
                else:
                    raise InvalidCodeException(code) from e
        return code

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "PyPixel"

    def generate_code(self, prompt: Prompt, model: Model) -> str:
        if not isinstance(model, Model):
            raise InvalidModelException(str(model))

        if not isinstance(prompt, Prompt):
            raise InvalidPromptException(str(prompt))

        response = model.run(prompt)
        code = self.extract_code(response)
        if messages := self.check_code(code):
            print(f"Warning: {messages}")
        return code

    @staticmethod
    def extract_code(text):
        if START not in text or END not in text:
            raise InvalidCodeException(text)

        if words := [word for word in BLACKLIST if word in text]:
            raise DangerousCodeException(text, words)
        return text.split(START)[1].split(END)[0]

    @staticmethod
    def write_to_file(code, file_name):
        with open(file_name, "w") as f:
            f.write(code)

    @staticmethod
    def check_code(code):
        print(code)
        messages = []
        tree = compile(code, "generated_code", "exec", ast.PyCF_ONLY_AST)
        checker = pyflakes.Checker(tree, "generated_code")
        for warning in checker.messages:
            message = f"{warning.__class__.__name__}: {warning.message % warning.message_args}"

            messages.append(message)
        return messages

    def generate_image(self, prompt, size, num_images, download=False):
        if not isinstance(self.model, OpenAI):
            raise InvalidModelException(
                "Invalid model for image generation. Only OpenAI supports image generation."
            )
        image_url = self.model.generate_image(
            GenerateImagePrompt(prompt), size, num_images
        )
        return self.download(download, image_url)

    def download(self, download, image_url):
        if download:
            self.download_image(image_url)
        else:
            logging.warning(
                "Image download is currently disabled. Use download=True to enable. Image URL expires in 60 minutes."
            )
        return image_url

    def edit_image(self, image, mask, prompt, n, size, download=False):
        if not isinstance(self.model, OpenAI):
            raise InvalidModelException(
                "Invalid model for image editing. Only OpenAI supports image editing."
            )
        image_url = self.model.edit_image(EditImagePrompt(prompt), image, mask, n, size)
        return self.download(download, image_url)

    @staticmethod
    def download_image(image_url):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        file_name = os.path.join(
            DOWNLOAD_DIR, datetime.now().strftime("%Y%m%d%H%M%S%f") + ".png"
        )
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            with open(file_name, "wb") as file:
                file.write(response.content)

            print(f"Image downloaded successfully: {file_name}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image: {e}")
