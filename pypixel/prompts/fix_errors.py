from ..constants import END, START
from .prompt import Prompt


class FixCode(Prompt):
    def __init__(self, prompt: str, code, errors):
        self.prompt = f"""
        You were given this prompt - "{prompt}". You generated this code - "{code}".
        The code you generated has errors - {errors}. Fix the errors in the code and return the fixed code.
        Return python code prefixed with {START} exactly and suffixed with {END} exactly to perform
        the operation from the prompt.
"""
        super().__init__(prompt=f"{self.prompt}")
