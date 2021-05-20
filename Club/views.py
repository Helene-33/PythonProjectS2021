from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event 

# Create your views here.
def index (request):
    return render(request, 'Club/index.html')

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list': meeting_list})

def meetingsdetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'Club/meetingsdetail.html', {'meetings' : meetings})

def meetingsminutes(request):
    meetingminutes_list=MeetingMinutes.objects.all()
    return render(request, 'Club/meetingsminutes.html', {'meetingminutes_list': meetingminutes_list})

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list': resource_list})

def events(request):
    event_list=Event.objects.all()
    return render(request, 'Club/events.html', {'event_list': event_list})
