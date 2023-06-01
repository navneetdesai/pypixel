import openai
import pytest

from pypixel import PyPixel
from pypixel.exceptions import *
from pypixel.models import Cohere, OpenAI, Starcoder
from pypixel.prompts import *


class TestPyPixel:
    pypixel_openai = PyPixel(OpenAI())
    pypixel_cohere = PyPixel(Cohere())
    pypixel_starcoder = PyPixel(Starcoder())

    def test_defaults(self):
        assert self.pypixel_openai.debug is False
        assert self.pypixel_openai.retries == 1

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
