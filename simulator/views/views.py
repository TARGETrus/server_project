from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class IndexView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html')


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')