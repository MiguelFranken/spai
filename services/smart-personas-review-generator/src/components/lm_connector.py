from langchain import OpenAI, PromptTemplate, HuggingFaceHub
from config import LLM_MODEL_NAME


class LLMConnectorFactory:
    """
    A factory class for creating language model connectors.

    This class provides a static method for creating a connector based on the LLM_MODEL_NAME configuration variable.
    Depending on the model name specified in the configuration:
    - If the LLM_MODEL_NAME starts with 'text-davinci', an OpenAIDavinciConnector is returned.
    - If the LLM_MODEL_NAME starts with 'flan-t5', a HuggingFaceConnector is returned.
    Otherwise, a ValueError is raised.

    Example usage:
    >>> connector = LLMConnectorFactory.create_connector()
    """

    @staticmethod
    def create_connector():
        if LLM_MODEL_NAME.startswith('text-davinci'):
            return OpenAIDavinciConnector()
        elif LLM_MODEL_NAME.startswith('flan-t5'):
            return HuggingFaceConnector()
        # Add more connectors as required
        raise ValueError(f"Unsupported LLM model: {LLM_MODEL_NAME}")


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


class HuggingFaceConnector:
    """
    A connector class for the google/flan-t5-xl language model via the HuggingFaceHub API.

    This class provides an interface for interacting with the google/flan-t5-xl language model through the
    HuggingFaceHub API.
    The `llm` attribute is an instance of the `HuggingFaceHub` class, which is used to generate text based on prompts.

    Attributes:
        llm (HuggingFaceHub): An instance of the HuggingFaceHub class representing the google/flan-t5-xl language model.
    """

    def __init__(self):
        self.llm = HuggingFaceHub(
            repo_id="google/flan-t5-xxl",
            model_kwargs={"temperature": 0.7}
        )

    @property
    def get_llm(self):
        """
        Returns the HuggingFaceHub language model instance associated with this connector.

        Returns:
            HuggingFaceHub: An instance of the HuggingFaceHub class representing the google/flan-t5-xl language model.
        """
        return self.llm
