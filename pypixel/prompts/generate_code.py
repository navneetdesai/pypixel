from prompt import Prompt


class GenerateCodePrompt(Prompt):
    prompt_template: str = """
    You are going to generate python3 code for the provided prompt.
    Return python code prefixed with <start> exactly and suffixed with <end> exactly to perform 
    the following operation on an image:
    """

    def __init__(self, prompt: str):
        super().__init__(prompt=f"{self.prompt_template} {prompt}")
