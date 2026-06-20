"""Project middleware placeholders."""


class RequestAuditMiddleware:
    """TODO: Add request auditing in Sprint B."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
