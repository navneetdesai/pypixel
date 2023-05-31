import pytest

from pypixel import prompts
from pypixel.exceptions import InvalidPromptException


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
