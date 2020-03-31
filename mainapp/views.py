from django.shortcuts import render
from django.views.generic import FormView
from .forms import ShorteningForm


class ShorteningView(FormView):
    template_name = 'homepage.html'
    form_class = ShorteningForm
    success_url = '/result/'

    def form_valid(self, form):
        return super().form_valid(form)


def result(request):
    return render(request, 'result.html')