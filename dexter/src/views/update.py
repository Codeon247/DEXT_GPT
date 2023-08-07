from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from src.controllers.dexcontroller import DexController
from src.lib.customresponse import CustomResponse
from django.core.exceptions import ValidationError

class UpdateDexView(generics.GenericAPIView):
    def post(self, requests):
        if "prompt_text" in requests.data:
            resp = DexController().custom_prompt(
                requests.data["prompt_text"], requests.data["instance_id"]
            )
        elif "prompt_id" in requests.data:
            resp = DexController().update_dex(
                requests.data["prompt_id"], requests.data["instance_id"]
            )
        else:
            raise ValidationError("Missing prompt_text/prompt_id")

        return CustomResponse(
            message="Dexter is ready to help",
            code=HTTP_200_OK,
            payload={ "instance_id": resp }
        )
