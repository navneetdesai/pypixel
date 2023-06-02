import pytest

from pypixelai import prompts
from pypixelai.exceptions import InvalidPromptException


class TestPrompts:
    def test_prompt(self):
        with pytest.raises(InvalidPromptException):
            prompts.Prompt()

    def test_fix_errors(self):
        with pytest.raises(InvalidPromptException):
            prompts.FixCodePrompt()
        with pytest.raises(InvalidPromptException):
            prompts.FixCodePrompt(prompt="test")
        with pytest.raises(InvalidPromptException):
            prompts.FixCodePrompt(code="print()")
        with pytest.raises(InvalidPromptException):
            prompts.FixCodePrompt(errors="TestException")

    def test_generate_code(self):
        with pytest.raises(InvalidPromptException):
            prompts.GenerateCodePrompt()

    def test_prompt_str(self):
        with pytest.raises(InvalidPromptException):
            str(prompts.Prompt())

        assert (
            str(prompts.GenerateCodePrompt(prompt="test"))
            == f"{prompts.GenerateCodePrompt.prompt_template} test"
        )
