import logging
import os
from django.http import JsonResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def root(request):
    logger.info("Root endpoint was called")
    return JsonResponse({"message": "Hello World from Django"})

def env_var_message(request):
    logger.info("env_var_message endpoint was called")
    message = os.getenv('MESSAGE', 'No message set')
    return JsonResponse({"message": message})

def env_var_number(request):
    logger.info("env_var_number endpoint was called")
    number = os.getenv('NUMBER', '0')
    return JsonResponse({"number": number})
