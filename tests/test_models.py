from django.test import TestCase
from core.models import Evento
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',
                                                         password='123456',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='123456')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

class EventoModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='123456', email='test@example.com')
        self.user.save()
        self.evento= Evento(titulo='Evento teste', descricao='Apenas um evento de teste',data_evento='2022-11-30',usuario=self.user)
        self.evento.save()

    def tearDown(self):
        self.user.delete()
        

    def test_read_evento(self):
        self.assertEqual(self.evento.usuario, self.user)
        self.assertEqual(self.evento.descricao, 'Apenas um evento de teste')
        self.assertEqual(self.evento.titulo, 'Evento teste')
        self.assertEqual(self.evento.data_evento,'2022-11-30')


    def test_update_evento_descricao(self):
        self.evento.descricao = 'new description'
        self.evento.save()
        self.assertEqual(self.evento.descricao, 'new description')
    

    def test_update_evento_titulo(self):
        self.evento.titulo = 'new title'
        self.evento.save()
        self.assertEqual(self.evento.titulo, 'new title')
    
    def test_update_evento_data_evento(self):
        self.evento.data_evento = '2022-12-05'
        self.evento.save()
        self.assertEqual(self.evento.data_evento, '2022-12-05')
    

'''
class EventoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
         usuario= User.objects.create(username='test', password='123456', email='test@example.com')
         Evento.objects.create(titulo='Evento teste', descricao='Apenas um evento de teste',data_evento='2022-11-30',usuario=usuario)

    def test_titulo(self):
        evento = Evento.objects.get(id=1)
        titulo = evento.titulo
        self.assertEqual(titulo, 'Evento teste')

'''