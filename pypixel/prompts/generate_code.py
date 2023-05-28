from ..constants import END, START
from .prompt import Prompt


class GenerateCodePrompt(Prompt):
    prompt_template: str = f"""
    You are going to generate python3 code for the provided prompt.
    You can only use the following libraries: {', '.join(Prompt.allowed_libraries)}.
    Return python code prefixed with {START} exactly and suffixed with {END} exactly to perform 
    the following operation on an image:
    """

    def __init__(self, prompt: str):
        super().__init__(prompt=f"{self.prompt_template} {prompt}")
