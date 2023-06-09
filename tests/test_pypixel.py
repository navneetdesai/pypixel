import sys
from io import StringIO

import pytest

from pypixelai import PyPixel
from pypixelai.constants import *
from pypixelai.exceptions import *
from pypixelai.models import Cohere, OpenAI, Starcoder


class TestPyPixel:
    pypixel_openai = PyPixel(OpenAI())
    pypixel_cohere = PyPixel(Cohere())
    pypixel_starcoder = PyPixel(Starcoder())

    def test_defaults(self):
        assert self.pypixel_openai.debug is False
        assert self.pypixel_openai.retries == 1

    def test_params(self):
        px = PyPixel(OpenAI(), debug=True, retries=2)
        assert px.debug is True
        assert px.retries == 2

    def test_representation(self):
        assert repr(self.pypixel_openai) == "PyPixel"
        assert str(self.pypixel_openai) == "PyPixel"

    def test_models(self):
        assert isinstance(self.pypixel_openai.model, OpenAI)
        assert isinstance(self.pypixel_cohere.model, Cohere)
        assert isinstance(self.pypixel_starcoder.model, Starcoder)

        assert self.pypixel_openai.model.model == "OpenAI"
        assert self.pypixel_cohere.model.model == "Cohere"
        assert self.pypixel_starcoder.model.model == "starcoder"

    def test_extract_code_exception(self):
        with pytest.raises(InvalidCodeException):
            self.pypixel_openai.extract_code("Hello world")
        with pytest.raises(InvalidCodeException):
            self.pypixel_openai.extract_code(f"{START}Hello world")
        with pytest.raises(InvalidCodeException):
            self.pypixel_openai.extract_code(f"Hello world{END}")

    def test_extract_dangerous_code(self):
        with pytest.raises(DangerousCodeException):
            self.pypixel_openai.extract_code(f"{START}exec{END}")

    def test_extract_code_with_blacklisted_words(self):
        """
        Extract code if the blacklisted keywords are not
        withing start and end tags
        :return:
        """
        assert self.pypixel_openai.extract_code(f"exec{START}print(){END}") == "print()"

    def test_extract_code(self):
        assert self.pypixel_openai.extract_code(f"{START}print(){END}") == "print()"
        assert (
            self.pypixel_openai.extract_code(
                f"Here is your code: {START}import cv2\nimport datetime{END}print()"
            )
            == "import cv2\nimport datetime"
        )

    def test_check_code(self):
        code = "print('Hello, world!')"
        expected_messages = []

        result = self.pypixel_openai.check_code(code)
        assert result == expected_messages

    def test_check_invalid_code(self):
        # invalid code
        code = "def test():\nprint(No indentation')"
        with pytest.raises(IndentationError):
            self.pypixel_openai.check_code(code)

        with pytest.raises(SyntaxError):
            self.pypixel_openai.check_code("Hello world")

        with pytest.raises(SyntaxError):
            self.pypixel_openai.check_code("print('Hello world'")

    def test_run_code(self):
        code = "print('Hello, world!')"
        capture = sys.stdout = StringIO()
        self.pypixel_openai.run_code(code)
        output = capture.getvalue()
        sys.stdout = sys.__stdout__
        assert output == "Hello, world!\n"

    def test_generate_code(self):
        prompt = "Write a function to add two numbers"
        with pytest.raises(InvalidModelException):
            self.pypixel_openai.generate_code(prompt, "InvalidModel")
