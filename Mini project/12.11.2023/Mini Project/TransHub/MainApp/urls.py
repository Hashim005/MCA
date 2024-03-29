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
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('validateGlobalEmail/', views.validateGlobalEmail, name="validateGlobalEmail"),
    path('check_username/', views.check_username, name='check_username'),
    path('check_email/', views.check_email, name='check_email'),
    path('StaffSignUp/', views.Staff_signUp, name='Staff_signUp'),
    path('adminhome/', views.Admin_Home, name='Admin_Home'),
    path('adminusertable/', views.user_account, name='user_account'),

    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),  
    
    #path('activate/<uidb64>/<token>',views.ActivateAccount.as_view(),name='activate'),
    path('deactivation_email/',views.activatation_email,name='activatation_email'),
    path('activation_email/',views.deactivation_email,name='deactivation_email'),

    path('update_profile/',views.update_profile,name='update_profile'),
    path('profile/',views.profile,name='profile'),
    path('category/',views.category_mgt,name='category-page'),
    path('save_category/',views.save_category,name='save-category'),
    path('manage-category', views.manage_category, name='manage-category'),
    path('manage-category/<int:pk>/', views.manage_category, name='manage-category'),
    path('delete_category',views.delete_category,name='delete-category'),
    path('location',views.location_mgt,name='location-page'),
    path('manage_location',views.manage_location,name='manage-location'),
    path('save_location',views.save_location,name='save-location'),
    path('manage_location/<int:pk>',views.manage_location,name='manage-location-pk'),
    path('delete_location',views.delete_location,name='delete-location'),
    path('bus',views.bus_mgt,name='bus-page'),
    path('manage_bus',views.manage_bus,name='manage-bus'),
    path('save_bus',views.save_bus,name='save-bus'),
    path('manage_bus/<int:pk>',views.manage_bus,name='manage-bus-pk'),
    path('delete_bus',views.delete_bus,name='delete-bus'),
    path('schedule',views.schedule_mgt,name='schedule-page'),
    path('manage_schedule',views.manage_schedule,name='manage-schedule'),
    path('save_schedule',views.save_schedule,name='save-schedule'),
    path('manage_schedule/<int:pk>',views.manage_schedule,name='manage-schedule-pk'),
    path('delete_schedule',views.delete_schedule,name='delete-schedule'),

]
