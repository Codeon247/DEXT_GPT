import json
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class ValidateRequestMiddleware(MiddlewareMixin):
    """
    Middleware for validating request data.
    """
    validation_dict = {
        "/login/": {
            "method": "POST", "required_keys": ["email", "password"]
        },
        "/signup/": {
            "method": "POST", "required_keys": ["email", "password"]
        },
        "/create/dex/": {
            "method": "POST", "required_keys": ["key"]
        },
        "/query/": {
            "method": "POST", "required_keys": ["instance_id", "query"]
        },
        "/change/prompt/": {
            "method": "POST", "required_keys": ["instance_id"]
        },
        "/add/prompt/": {
            "method": "POST", "required_keys": ["prompt_text", "prompt_name"]
        }
    }

    def validate(self, required, provided):
        for key in required:
            if key not in provided:
                return JsonResponse({"code": 404, "message": f"missing {key}", "payload": None, "status": False}, status=404)

    def process_request(self, request):
        """
        Validate request data based on the provided URL.

        Args:
            request: Django request object

        Raises:
            ValidationError: If required key(s) are missing from the request data.
        """
        method = request.method
        url = request.path_info
        validation_config = self.validation_dict.get(url)

        if validation_config and validation_config.get("method") == method:
            required_keys = validation_config.get("required_keys")
            if method == "POST":
                self.validate(required_keys, json.loads(request.body))

