from django.test import TestCase
from core.models import Evento
from django.contrib.auth import get_user_model
from django.urls import reverse


class SignInViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',
                                                         password='123456',
                                                         email='test@example.com')

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        self.client.login(username='test',password='123456',)
        response = self.client.post('/login/submit', {'username': 'test', 'password': '123456'})
        self.assertRedirects(response, '/', target_status_code=302)


