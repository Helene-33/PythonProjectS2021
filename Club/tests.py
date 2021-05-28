from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, meetings, meetingsdetail, meetingsminutes, resources, events
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class MeetingTest(TestCase):
   def setUp(self):
       type=Meeting(meetingtitle="Firstmeeting")
       meeting=Meeting(meetingtitle="Firstmeeting", meetingdate="25th May 2021", meetingtime="11am")
       return meeting
   def test_string(self):
       meet = self.setUp()
       self.assertEqual(str(meet), meet.meetingtitle)
   def test_type(self):
       meet=self.setUp()
       self.assertEqual(str(meet.meetingdate), '25th May 2021')

   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
   def test_string(self):
       type=MeetingMinutes(minutestext="Jeff's job")
       self.assertEqual(str(type), type.minutestext)

   def test_table(self):
       self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')


class ResourceTest(TestCase):
   def test_string(self):
       res=Resource(resourcename="New website")
       self.assertEqual(str(res), res.resourcename)

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')


class EventTest(TestCase):
   def test_string(self):
       eve=Event(eventtitle="Luch the new website")
       self.assertEqual(str(eve), eve.eventtitle)

   def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class MeetingTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meetings'))
       self.assertEqual(response.status_code, 200)


def setUp(self):
        self.u=User.objects.create(username='myuser')
        self.type=Meeting.objects.create(meetingtitle='Firstmeeting')
        self.meet = Meeting.objects.create(meetingtitle='Firstmeeting', meetingtype=self.type, user=self.u, meetingdate="25th May 2021", meetingtime='11am')
        self.res=Resource.objects.create(resourcename='New website')
        self.eve = Event.objects.create(eventtitle='Luch the new website')


def test_meeting_detail_success(self):
        response = self.client.get(reverse('meetingdetails', args=(self.meet.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)
     