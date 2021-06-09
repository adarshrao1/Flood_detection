from django.urls import path
from backend.views import adminpage, home, loginPage, registerPage, logoutUser

urlpatterns = [
    path('', home, name='home'),
    path('adminpanel/', adminpage, name='admin'),
    path('login/', loginPage, name='login'),
    path('signup/', registerPage, name='signup'),
    path('logout/', logoutUser, name='logout')
]
