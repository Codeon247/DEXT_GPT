from src.dexai import Dex
from django.core.exceptions import ValidationError

from src.dexai.prompts.customprompt import CustomPrompt
from src.models import Prompt


class DexController:
    """
    Controller for handling operations related to the Dex AI interface.
    """

    def prepare_dexter(self, openaikey):
        """
        Prepares a Dex AI instance using the provided OpenAI key.

        Args:
            openaikey (str): OpenAI API key.

        Returns:
            Dex object prepared for further actions.
        """
        dexter = Dex(openaikey)
        return dexter.prepare_dextor()

    def ask_dexter(self, requestData):
        """
        Query the Dex AI instance with provided data.

        Args:
            requestData (dict): Dictionary containing instance ID and query text.

        Returns:
            Response from the Dex AI instance.

        Raises:
            ValidationError: If instance ID or query text is missing.
            ValidationError: If an error occurs during processing the query.
        """
        # Extract instance ID and query from the request data
        instance_id = requestData.get("instance_id")
        query = requestData.get("query")

        # Validate that instance ID and query are present
        if not instance_id:
            raise ValidationError("Missing instance ID")
        if not query:
            raise ValidationError("Missing query text")

        try:
            # Send the query to the Dex AI instance and return the response
            return Dex().query(instance_id, query)
        except Exception as e:
            raise ValidationError(f"Unable to process query, error: {e}")

    def status(self, instance_id):
        """
        Check the status of a Dex AI instance.

        Args:
            instance_id (str): ID of the Dex AI instance.

        Returns:
            Status of the Dex AI instance.
        """
        status = Dex().checkInstanceStatus(instance_id)
        return {"instance_id": instance_id, "status": status }

    def custom_prompt(self, text, instance_id):
        """
        Update prompts to Dex AI instance

        Args:
            prompt_id (str): Id of prompt to be applied to instance.
            instance_id (str): AI Instance ID.

        Returns:
            Dex object prepared for further actions.
        """
        prompt = CustomPrompt(text)
        return Dex().update_instance(prompt, instance_id)

    def update_dex(self, prompt_id, instance_id):
        """
        Update prompts to Dex AI instance

        Args:
            prompt_id (str): Id of prompt to be applied to instance.
            instance_id (str): AI Instance ID.

        Returns:
            Dex object prepared for further actions.
        """
        promptsObjs = Prompt.objects.filter(id=prompt_id)
        if promptsObjs.count() < 1:
            raise ValidationError(f"Prompt with id : {prompt_id} does not exits")

        prompttext = promptsObjs[0].prompt_text
        prompt = CustomPrompt(prompttext)
        return Dex().update_instance(prompt, instance_id)