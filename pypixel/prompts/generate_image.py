from ..constants import END, START
from ..exceptions import InvalidPromptException
from .prompt import Prompt


class GenerateImagePrompt(Prompt):
    # Prompt to Dall-E for image generation:
    prompt_template: str = """
    You will be given the description of an image. Analyze the context from the description and generate the image.
    Here is the description:
    """

    def __init__(self, prompt: str = None):
        if not prompt:
            raise InvalidPromptException(prompt)
        super().__init__(prompt=f"{self.prompt_template} {prompt}")
