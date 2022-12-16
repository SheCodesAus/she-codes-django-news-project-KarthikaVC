from django.urls import path
from .views import CreateAccountView, EditProfilePageView,PasswordsChangeView
from .views import ProfileView

# Added by Karthika V 
from django.contrib.auth import views as auth_views
from . import views

app_name ='users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/view-profile',ProfileView.as_view(),name='viewAccount'),
    path('edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile_page'),
    path('change-password/', PasswordsChangeView.as_view(),name='change-password'),
    path('password_success',views.password_success,name='password_success'),
]