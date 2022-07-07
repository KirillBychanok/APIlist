from django.test import TestCase

from .models import Tickets


class TestTicketsModel(TestCase):
    """Тестирование модели Tickets"""
    def setUp(self):
        self.p = Tickets(title='вопрос', content='проблема',)

    def test_create_tickets(self):
        self.assertIsInstance(self.p, Tickets)

    def test_str_representation(self):
        self.assertEqual(str(self.p), 'вопрос')

