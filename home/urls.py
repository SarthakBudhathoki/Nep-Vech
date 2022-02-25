from unicodedata import name
from django.urls import path
from .views import home, about, service, book, buy,contact,buyfinal,admin,addproduct,viewmessage
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('book/', book, name='book'),
    path('buy/<int:p_id>', buy , name='buy'),
    path('buyfinal',buyfinal, name= 'buyfinal'),
    path('contact/', contact, name='contact'),
    path('admin',admin, name='admin'),
    path('addproduct',addproduct, name='addproduct'),
    path('viewmessage',viewmessage, name= 'viewmessage')
]