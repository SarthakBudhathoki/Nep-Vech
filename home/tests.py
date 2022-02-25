 
 
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

    def test_buyfinal_url(self):
        url=reverse("buyfinal")
        self.assertEquals(resolve(url).func,buyfinal)  

    def test_viewmessage_url(self):
        url=reverse("viewmessage")
        self.assertEquals(resolve(url).func,viewmessage)  

    def test_addproduct_url(self):
        url=reverse("addproduct")
        self.assertEquals(resolve(url).func,addproduct)  

    def test_admin_url(self):
        url=reverse("admin")
        self.assertEquals(resolve(url).func,admin)  

    def test_buy_url(self):
        url=reverse("buy", args=[1])
        self.assertEquals(resolve(url).func,buy)        