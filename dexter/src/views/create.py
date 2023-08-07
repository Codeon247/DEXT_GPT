from rest_framework import generics
from src.controllers.dexcontroller import DexController
from src.lib.customresponse import CustomResponse

class CreateDexView(generics.GenericAPIView):
    def post(self, requests):

        try:
            instance_id = DexController().prepare_dexter(requests.data.get("key"))
        except Exception as e:
            instance_id = str(e)
        return CustomResponse(
            message="Dexter is ready to help",
            code=200,
            payload = {"instance_id": instance_id}
        )