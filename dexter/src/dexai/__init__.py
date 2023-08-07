# DexGPT @ autobotpy technologies private limited.
# Author : scoder91@gmail.com

# Importing the necessary module
import re
import uuid
from django.core.cache import cache

from src.dexai.model import TextDavinci
from src.dexai.prompts.basic import get_basic_prompt_template
from src.dexai.utils import DexMemory, CreateConversationChainWithMemory

class Dex:
    """
    Dex - The AI assistant for developers.
    Dex is an AI agent that aids developers with their development-related tasks.
    The AI agent can list down tasks and perform them one by one on the user's system,
    based on the user's approval.
    """

    def __init__(self, openaikey=None) -> None:
        """
        Dex constructor - Initializes Dex's state.
        Dex already has a brain; we're just adding storage capabilities here.
        """
        if openaikey != None:
            self.openaikey = openaikey

    def getInstanceId(self):
        """
        :return: Unique ID for dexter instance.
        """
        return str(uuid.uuid4())

    def prepare_dextor(self):
        """
        Prepares the Dexter for the user.

        Returns: ConversationChain with memory and prompt ready to help the developers
        """

        self.dex_memory = DexMemory().memory
        self.dex_model = TextDavinci(self.openaikey).model
        self.prompt = get_basic_prompt_template()

        self.instance = CreateConversationChainWithMemory(
            self.dex_model, self.dex_memory, self.prompt
        )

        return self.setInstance(key=self.openaikey)

    def update_instance(self, prompt, instanceID):
        self.openaikey = cache.get(instanceID + "-key")
        print ("Got open ai key", self.openaikey)

        self.dex_memory = DexMemory().memory
        self.dex_model = TextDavinci(self.openaikey).model

        self.instance = CreateConversationChainWithMemory(
            self.dex_model, self.dex_memory, prompt
        )

        return self.setInstance(instanceID=instanceID)

    def query(self, instanceID, query):
        """

        :param instanceID: ID of instance
        :param query:
        :return:
        """
        self.instance = cache.get(instanceID)
        if self.instance is None:
            return False

        resp = self.instance.run(query)
        self.setInstance(instanceID=instanceID)
        return resp

    def setInstance(self, instanceID=None, key=None):
        if instanceID == None:
            instanceID = self.getInstanceId()

        if key:
            print ("Save Open AI Key", key)
            cache.set(instanceID + "-key", key)

        cache.set(instanceID, self.instance)
        return instanceID

    def checkInstanceStatus(self, instanceID):
        instance = cache.get(instanceID)
        if not instance:
            return False
        return True


