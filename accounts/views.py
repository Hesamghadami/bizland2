from django.shortcuts import render , get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import  Profile
from .forms import AuthenticationForm,EditProfile,CustomUserCreation
from django.views.generic import FormView, CreateView, UpdateView, TemplateView



class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def form_valid(self, form):
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)


class LogOutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreation
    success_url = '/accounts/login/' #'registration/login' 

    def form_valid(self, form):
        form.save()
        email = self.request.POST.get('email')
        password = self.request.POST.get('password1')   
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request,user)
            return redirect('/accounts/edit-profile/%i'%(user.id-1))
        
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Invalid email or password')
        return super().form_invalid(form)



def edit_profile(request, pk):
    if request.method == 'GET':
        form = EditProfile()
        return render(request,'registration/edit_profile.html', context={'form': form})
    elif request.method == 'POST':
        profile = Profile.objects.get(user=pk)
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
                form.save()
    return redirect('root:home')
            
