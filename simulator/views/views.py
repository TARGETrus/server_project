from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='/simulator/login/'), name='get')
class IndexView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html')
