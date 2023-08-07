from langchain import OpenAI

class TextDavinci:
    """
    TextDavinci - An OpenAI model class.

    This class wraps around the OpenAI API using the langchain module to facilitate
    easy interaction with the OpenAI text-davinci-003 model.
    """

    def __init__(self, api_key: str, temperature: float = 1, model_name: str = "gpt-3.5-turbo-0613") -> None:
        """
        TextDavinci constructor - Initializes the OpenAI model with provided API key.

        Args:
        api_key (str): OpenAI API key.
        temperature (float): The temperature parameter for the OpenAI API. Default is 0.
        model_name (str): The OpenAI model name. Default is "text-davinci-003".
        """
        self.api_key = api_key
        self.temperature = temperature
        self.model_name = model_name
        self.openai_model = None

    @property
    def model(self) -> OpenAI:
        """
        Creates and returns an instance of the OpenAI model.

        Returns:
        OpenAI: An instance of the OpenAI model.
        """
        if not self.openai_model:
            self.openai_model = OpenAI(
                temperature=self.temperature,
                openai_api_key=self.api_key
            )

        return self.openai_model