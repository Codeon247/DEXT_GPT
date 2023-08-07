from langchain.memory import ConversationBufferMemory

class DexMemory:
    """
    DexMemory - A conversation memory class for Dex.
    """

    def __init__(self) -> None:
        """
        DexMemory constructor - Initializes the DexMemory
        """
        self.dex_memory = None

    @property
    def memory(self) -> ConversationBufferMemory:
        """
        Creates and returns an instance of ConversationSummaryMemory.

        Returns:
        ConversationSummaryMemory: An instance of ConversationSummaryMemory.
        """
        if not self.dex_memory:
            self.dex_memory = ConversationBufferMemory()

        return self.dex_memory
