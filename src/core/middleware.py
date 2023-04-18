# middleware.py
from .models import Visitor


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Only log requests to non-static files
        if not request.path.startswith('/static/'):
            Visitor.objects.create(ip_address=request.META['REMOTE_ADDR'])

        return response
