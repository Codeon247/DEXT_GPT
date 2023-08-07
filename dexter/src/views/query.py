from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from src.controllers.dexcontroller import DexController
from src.lib.customresponse import CustomResponse

class QueryDexView(generics.GenericAPIView):
    def post(self, requests):
        Response = DexController().ask_dexter(requests.data)
        return CustomResponse(
            message="Dexter is talking",
            payload=Response,
            code=HTTP_200_OK
        )
