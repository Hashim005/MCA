from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('', views.showIndex, name='showindex'),
    path('SignUp/', views.SignUp,name='signup'),
    path('about/', views.about, name='about'),
    path('login/', views.Log, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.Home, name='Home'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete')

]
