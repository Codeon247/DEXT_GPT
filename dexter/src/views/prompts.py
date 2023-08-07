from rest_framework import generics
from src.lib.customresponse import CustomResponse
from src.controllers.promptcontroller import PromptController

class PromptView(generics.GenericAPIView):

    def get(self, requests):
        return CustomResponse(
            message="All Prompts", code=200, payload=PromptController().getAllPrompts()
        )