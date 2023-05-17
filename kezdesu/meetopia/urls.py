from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("history", MeetingsView.as_view(), name='history' ),   # история
    path('portfolio', ProfilePageView.as_view(), name='portfolio'),   #портфолио
    path('contact', ContactPageView.as_view(), name='contact'),    #контакт
    path('meeting/<code>', MeetingView.as_view(), name='meeting'),   #можно называть и креате
    path('meeting_res', CreateView.as_view(), name='create'),    #create !!!
    path('result/<code>', ResultView.as_view(), name='success'),  # успешно сохранились!
    path('meeting_join', MeetingJoinView.as_view(), name='meeting_join'),
    path('generate_code', GenerateCodeView.as_view(), name='generate_code'),   #функция уникальный код
    path('admin/', admin.site.urls),
    
]