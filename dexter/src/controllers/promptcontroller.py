from django.core.exceptions import ValidationError
from src.serializers.promptsserializer import Prompt, PromptSerializer

class PromptController:
    """
    Controller class for handling operations related to Prompt objects.
    """

    def create(self, promptData):
        """
        Create a new Prompt object.

        Args:
            promptData: The serialized data for creating a Prompt object.

        Returns:
            Serialized data of the newly created Prompt object.

        Raises:
            ValidationError: If required prompt name or text is missing.
        """
        # Extract prompt text and name from the request data
        text = promptData.data.get("prompt_text")
        name = promptData.data.get("prompt_name")

        # Validate that prompt text and name are present also prompt name is unique.
        if not text:
            raise ValidationError("Missing prompt text")
        if not name:
            raise ValidationError("Missing prompt name")
        if self.getPromptByName(name):
            raise ValidationError(f"prompt with name {name} already exits")

        # Create a new prompt with provided data
        prompt = Prompt.objects.create(prompt_text=text, prompt_name=name, created_by=promptData.user)

        # Return the serialized data of the new prompt
        return PromptSerializer(prompt).data

    def getAllPrompts(self):
        """
        Fetch all Prompt objects.

        Returns:
            List of all serialized Prompt objects.
        """
        # Get all prompts from the database and serialize them
        all_prompts = Prompt.objects.all()

        # Return the serialized data
        return PromptSerializer(all_prompts, many=True).data

    def getPromptById(self, id):
        """
        Fetch a specific Prompt object by its ID.

        Args:
            id: The ID of the Prompt object.

        Returns:
            Serialized data of the fetched Prompt object.

        Raises:
            ValidationError: If a prompt with the given ID doesn't exist.
        """
        # Try to get the prompt with the given ID
        prompt = Prompt.objects.filter(id=id).first()

        # If the prompt doesn't exist, raise an error
        if not prompt:
            raise ValidationError(f"Prompt with ID {id} does not exist")

        # Return the serialized data of the fetched prompt
        return PromptSerializer(prompt).data

    def getPromptByName(self, name):
        """
        Fetch a specific Prompt object by its Name.

        Args:
            name: The Name of the Prompt object.

        Returns:
            Serialized data of the fetched Prompt object.

        Raises:
            ValidationError: If a prompt with the given Name doesn't exist.
        """
        # Try to get the prompt with the given name
        prompt = Prompt.objects.filter(prompt_name=name).first()

        # If the prompt doesn't exist, raise an error
        if not prompt:
            return False

        # Return the serialized data of the fetched prompt
        return PromptSerializer(prompt).data
