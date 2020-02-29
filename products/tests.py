from django.test import TestCase
from django.urls import reverse
from .models import Product

# Create your tests here.
class ProductTest(TestCase):

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)