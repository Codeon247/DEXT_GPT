from rest_framework.permissions import IsAuthenticated
from src.lib.customresponse import CustomResponse
from rest_framework import generics
from src.controllers.promptcontroller import PromptController

class AddPromptView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def post(self, requests):
        Response = PromptController().create(requests)
        return CustomResponse(
            message="prompt added successfully", code=200, payload=Response
        )