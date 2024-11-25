import logging

logger = logging.getLogger(__name__)

class DebugRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request details
        logger.debug(f"Request Path: {request.path}")
        logger.debug(f"Request Method: {request.method}")
        logger.debug(f"Request Headers: {request.headers}")
        
        response = self.get_response(request)
        
        # Log response details
        logger.debug(f"Response Status: {response.status_code}")
        if response.status_code >= 400:
            logger.error(f"Error Response Content: {getattr(response, 'content', '')}")
        
        return response

    def process_exception(self, request, exception):
        logger.error(f"Exception occurred: {exception}")
        return None