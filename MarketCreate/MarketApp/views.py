import json, bcrypt, jwt, re

from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import User
# from django.shortcuts import render


# Create your views here.
class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email = data['email']
            password = data['password']

         except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
