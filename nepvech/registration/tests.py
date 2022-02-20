from codecs import register
from django.urls import reverse,resolve
from django.test import SimpleTestCase
from .views import *

class TestUrls(SimpleTestCase):
    def test_signup_url(self):
        url=reverse("signup")
        self.assertEquals(resolve(url).func,signup)

    

        


