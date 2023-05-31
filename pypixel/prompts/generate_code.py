from ..constants import END, START
from .prompt import Prompt


class GenerateCodePrompt(Prompt):
    prompt_template: str = f"""
    You are going to generate python3 code for the provided prompt. You can only use the following libraries: {', '.join(Prompt.allowed_libraries)}. Do not change or alter any other features of the image. Only and only do as much is required to perform the operation on the image. Do not perform any other operation on the image. Only return one solution. Verify that the code has no errors before returning it. Return python code prefixed with {START} exactly and suffixed with {END} exactly to perform the following operation on an image:
    """

    def __init__(self, prompt: str):
        super().__init__(prompt=f"{self.prompt_template} {prompt}")
