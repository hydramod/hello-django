from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_done_default_to_false(self):
        item = Item.objects.create(name='Test Item')
        self.assertFalse(item.done)
