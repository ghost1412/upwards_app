from rest_framework.exceptions import ValidationError, ParseError
from django.http import HttpResponseServerError
from django.http import Http404
import json
from django.http import JsonResponse

def api_view(request):
    raise ValidationError

def create_5xx_view(request):
    return HttpResponseServerError(json.dumps({'error': 'An error occured'}))

def create_2xx_view(request):
    data = {
        "success": 'True'
    }
    return JsonResponse(data)

def create_4xx_view(request):
    raise Http404