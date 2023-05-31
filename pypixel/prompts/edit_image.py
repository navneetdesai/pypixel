from ..exceptions import InvalidPromptException
from .prompt import Prompt


class EditImagePrompt(Prompt):
    prompt_template: str = """
    You will be given an image, a mask, and a description of the new image. You must edit the image to match the description.
    """

    def __init__(self, prompt: str = None):
        if not prompt:
            raise InvalidPromptException(prompt)
        super().__init__(prompt=f"{self.prompt_template} {prompt}")
