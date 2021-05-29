from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingsdetail/<int:id>', views.meetingsdetail, name='detail'),
    path('meetingsminutes/', views.meetingsminutes, name='meetingsminutes'),
    path('resources/', views.resources, name='resources'),
    path('events/', views.events, name='events'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
]
