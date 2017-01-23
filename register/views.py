from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.urls import reverse

from .forms import RegistrationForm


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] and form.cleaned_data['password2']:
                if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                    user = User.objects.create_user(
                        form.cleaned_data['username'],
                        form.cleaned_data['email'],
                        form.cleaned_data['password1'],
                        )
                    user.save()
            return render(request, 'registration/success.html', {})
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    return HttpResponseRedirect(reverse('calculator:budget_edit'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))
