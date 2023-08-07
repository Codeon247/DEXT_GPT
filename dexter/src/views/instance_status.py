from rest_framework import generics
from src.lib.customresponse import CustomResponse
from src.controllers.dexcontroller import DexController

class InstanceStatusView(generics.GenericAPIView):

    def post(self, requests):

        status = DexController().status(
            requests.data.get("instance_id")
        )
        return CustomResponse(message="All Prompts", code=200, payload=status)