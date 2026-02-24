"""
Views for the core Django application.
"""

import logging
from django.http import HttpResponse
from django.http import HttpRequest


logger = logging.getLogger(__name__)


def hello_world(request: HttpRequest) -> HttpResponse:
    """
    Return a simple hello world response.

    Args:
        request: The HTTP request object.

    Returns:
        An HttpResponse with a hello world message.
    """
    logger.info("Hello world view accessed")
    return HttpResponse("Hello, World!")
