from ..constants import ALLOWED_LIBRARIES


class Prompt:
    """
    Base class for all prompts
    """

    prompt: str = None
    allowed_libraries: tuple[str] = ALLOWED_LIBRARIES

    def __init__(self, prompt):
        self.prompt = prompt

    def __str__(self):
        if not self.prompt:
            raise NotImplementedError("Prompt not implemented")
        return self.prompt

    def __repr__(self):
        return self.__str__()
