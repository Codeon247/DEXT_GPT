from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from src.lib.customresponse import CustomResponse
from src.controllers.usercontroller import UserController

class SignupView(generics.GenericAPIView):
    def post(self, request):
        Response = UserController().signup(request.data.get("email"), request.data.get("password"))
        return CustomResponse(message="Signup API View", payload=Response, code=HTTP_200_OK)
