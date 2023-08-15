from langchain import OpenAI

from config import LLM_MODEL_NAME


class OpenAIDavinciConnector:
    """
    A connector class for OpenAI's Davinci language model.

    This class provides an interface for interacting with the Davinci language model through the OpenAI API.
    The `llm` attribute is an instance of the `OpenAI` class, which is used to generate text based on prompts.

    Attributes:
        llm (OpenAI): An instance of the OpenAI class representing the Davinci language model.
    """

    def __init__(self):
        self.llm = OpenAI(
            model_name=LLM_MODEL_NAME,
            temperature=0.7,
        )

    @property
    def get_llm(self):
        """
        Returns the OpenAI language model instance associated with this connector.

        Returns:
            OpenAI: An instance of the OpenAI class representing the Davinci language model.
        """
        return self.llm
