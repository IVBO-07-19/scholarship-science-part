
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import psycopg2

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
def get_first(request):
    if request.method == "GET":
        message_list = []
        #for p in MyProject.objects.raw('SELECT id, place, status FROM simple_myproject'):
            #message_list.append({'id': p.id, 'place': p.place, 'status': p.status})
        #return JsonResponse(test_list, safe=False)

    elif request.method == "POST":
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_index(request, id):
    return JsonResponse(serializer.data, safe=False)