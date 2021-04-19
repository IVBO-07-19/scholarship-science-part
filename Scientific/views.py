
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import psycopg2
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


from Scientific.models import Scientific_Research_Work, Patent, Grant, Publications

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def get_data(request):
    if request.method == 'GET':
        grant_list = []
        publications_list = []
        patent_list = []
        research_work_list = []
        user_id = '1'
        
        for p in Grant.objects.filter(user=user_id):
            grant_list.append({"title": p.title, 'individual_team': p.individual_team, 'RTU_reward': p.RTU_reward, 'date': p.date, 'scores': (p.scores if p.scores > -1 
            else 0)})
        for p in Publications.objects.filter(user=user_id):
            publications_list.append({'title': p.title, 'volume_title': p.volume_title, 'level': p.level, 'authors_quantity': p.authors_quantity, 'date': p.date, 'scores': (p.scores if p.scores > -1 
            else 0)})
        for p in Patent.objects.filter(user=user_id):
            patent_list.append({'title': p.title, 'individual_team': p.individual_team, 'RTU_reward': p.RTU_reward, 'date': p.date, 'scores': (p.scores if p.scores > -1 
            else 0)})
        for p in Scientific_Research_Work.objects.filter(user=user_id):
            research_work_list.append({'title': p.title, 'place': p.title, 'individual_team': p.individual_team, 'RTU_reward': p.RTU_reward, 'date': p.date, 'scores': (p.scores if p.scores > -1 
            else 0)})
        
        return JsonResponse({'Grants': grant_list, 'Publications': publications_list, 'Patents': patent_list, 'Research_works': research_work_list}, safe=False)


@api_view(['GET', 'POST'])
def add_grants(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        grant = Grant()

        grant.title = data['title']
        grant.individual_team = data['individual_team']
        grant.RTU_reward = data['RTU_reward']

        grant.date = data['date']
        grant.user = data['user']
        
        grant.save()
        return JsonResponse({'Status': 'Confirmed'})

@api_view(['GET', 'POST'])
def add_patents(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        patent = Patent()

        patent.title = data['title']
        patent.individual_team = data['individual_team']
        patent.RTU_reward = data['RTU_reward']

        patent.date = data['date']
        patent.user = data['user']
        
        patent.save()
        return JsonResponse({'Status': 'Confirmed'})

@api_view(['GET', 'POST'])
def add_publications(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        publication = Publication()

        publication.title = data['title']
        publication.volume_title = data['volume_title']
        publication.level = data['level']
        publication.authors_quantity = data['authors_quantity']

        publication.date = data['date']
        publication.user = data['user']
        
        publication.save()
        return JsonResponse({'Status': 'Confirmed'})

@api_view(['GET', 'POST'])
def add_scientific_research_works(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        scientific_research_work = Scientific_Research_Work()

        scientific_research_work.title = data['title']
        scientific_research_work.place = data['place']
        scientific_research_work.individual_team = data['individual_team']
        scientific_research_work.RTU_reward = data['RTU_reward']

        scientific_research_work.date = data['date']
        scientific_research_work.user = data['user']
        
        scientific_research_work.save()
        return JsonResponse({'Status': 'Confirmed'})