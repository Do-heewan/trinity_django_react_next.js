from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

def hello(request):
    return HttpResponse("Hello, Django!")

@api_view(["GET", "POST"])
def hello_rest_api(request):
    data = {"message" : "Hello REST API"}
    return Response(data)