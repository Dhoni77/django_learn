from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from .models import Candidate
from .views import greeting_view
# Create your tests here.

class TestCandidate(TestCase):
    ''' Test the Candidate model '''
    def setUp(self):
        self.c = Candidate(name='Arun', website='www.arun.com', email='contact@arun.com')

    def test_create_candidate(self):
        self.assertIsNotNone(self.c, Candidate)

    def test_str_representation(self):
        self.assertEquals(str(self.c), 'Arun')

class TestGretingView(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='test user', password='test@123')
        test_user.save()
        self.client = Client()

    def test_greeting_user_not_authenticated(self):
        response = self.client.get('/test/greeting')
        self.assertEquals(response.status_code, 302)

    def test_greeting_user_authenticated(self):
        login = self.client.login(username='test user', password='test@123')
        response = self.client.get('/test/greeting')
        self.assertEquals(response.status_code, 200)

class TestGreetingViewRequestFactory(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser', password='test@123')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_greeting_not_authenticated(self):
        request = self.factory.get('/test/greeting')
        request.user = AnonymousUser()
        response = greeting_view(request)
        self.assertEquals(response.status_code, 302)

    def test_user_greeting_authenticated(self):
        request = self.factory.get('/test/greeting')
        request.user = self.test_user
        response = greeting_view(request)
        self.assertEquals(response.status_code,  200)