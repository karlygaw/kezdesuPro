from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from django.utils.crypto import get_random_string
from .forms import * 
from .models import *

import openai
from django.conf import settings
from django.http import JsonResponse

class MeetingsView(View):
    '''История встреч'''
    def get(self, request):
        meetings = MeetingSphere.objects.all()
        return render(request, "kezdesu/history.html", {"meetings_list": meetings})

class HomePageView(View):
    def get(self, request):
        return render(request, 'kezdesu/index.html')
    
class ContactPageView(View):
    def get(self, request):
        return render(request, 'kezdesu/contact.html')
    
class ProfilePageView(View):
    def get(self, request):
        return render(request, 'kezdesu/profile.html')
    
class GenerateCodeView(View):
    def post(self, request):
        if request.method == 'POST':
            code = str(uuid.uuid4())[:8].replace('-', '').upper()
            #code = get_random_string(length=10)
            #code_obj = MeetingSphere.objects.create(code=code)
        return redirect('meeting', code=code)
    
    
class MeetingView(View):
    def get(self, request, code):
        categories = Category.objects.all()
        cuisines = Cuisine.objects.all()
        places = Place.objects.all()

        meeting_data = {
            'code': code,
            'categories': categories,
            'cuisines': cuisines,
            'places': places,
        }
        return render(request, 'kezdesu/getcode.html', context=meeting_data)
    
class CreateView(View):
    def post(self, request):
        if request.method == "POST":
                meeting = MeetingSphere()
                meeting.code = request.POST.get("code")
                code = meeting.code
                meeting.name = request.POST.get("name")
                meeting.message = request.POST.get("message")
                meeting.date = request.POST.get("date")
                meeting.place = request.POST.get("place")
                meeting.cuisine = request.POST.get("cuisine")
                meeting.cat = request.POST.get("cat")
                meeting.save()
        return redirect('success', code=code)

class ResultView(View):
    def get(self, request, code):
        categories = Category.objects.all()
        cuisines = Cuisine.objects.all()
        places = Place.objects.all()

        meeting_data = {
            'code': code,
            'categories': categories,
            'cuisines': cuisines,
            'places': places,
        }

        return render(request, 'kezdesu/success.html', context=meeting_data)
    
class MeetingJoinView(View):
    # def get(self, request, code):
    #     return render(request, 'kezdesu.html', {'code': code})

    def post(self, request):
        entered_code = request.POST.get('code')

        try:
            meeting = MeetingSphere.objects.get(code=entered_code)
            # Код существует в базе данных, выполнить действия
            return redirect('meeting', code=entered_code)  # Перенаправление на страницу успеха
        except MeetingSphere.DoesNotExist:
            # Код не существует в базе данных, выполнить действия
            return redirect('failure') 


#openai

