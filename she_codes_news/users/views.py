from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView 
# Added by Karthika V
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render

from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import EditUserProfileForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

# Create your views here.
class ProfileView(generic.DetailView):
	model = CustomUser
	template_name = 'users/viewAccount.html'
	# context_object_name = 'profile'

class EditProfilePageView(UpdateView):
    form_class = EditUserProfileForm
    template_name = 'users/edit_profile_page.html'
    success_url = reverse_lazy('users:viewAccount')

    def get_success_url(self):
        print(self.request.user.id)
        print(type(self.get_form()))
        return reverse_lazy('users:viewAccount', kwargs={"pk":self.request.user.id})

    def get_object(self):
        return self.request.user
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name ='users/change-password.html'
    success_url = reverse_lazy('users:password_success')

def password_success(request):
    return render(request,'users/password_success.html',{})