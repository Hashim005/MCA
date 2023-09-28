from django.urls import path
from . import views

urlpatterns = [
    path('', views.showIndex, name='showindex'),
    path('SignUp/', views.SignUp,name='signup'),
    path('about/', views.about, name='about'),
    path('Login/', views.Login, name='login'),
    #path('Logout/', views.Logout_user, name='logout_user'),
    path('home/', views.Home, name='Home')
]
