 
 
from codecs import register
from django.urls import reverse,resolve
from django.test import SimpleTestCase
from .views import *

class TestUrls(SimpleTestCase):
    def test_about_url(self):
        url=reverse("about")
        self.assertEquals(resolve(url).func,about)

    def test_service_url(self):
        url=reverse("service")
        self.assertEquals(resolve(url).func,service)    

    def test_book_url(self):
        url=reverse("book")
        self.assertEquals(resolve(url).func,book) 

    def test_contact_url(self):
        url=reverse("contact")
        self.assertEquals(resolve(url).func,contact)         