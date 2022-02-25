from django.urls import path
from .views import signup, LoginView,logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',logout, name = 'logout' )
]