from django.http import HttpResponseRedirect
from django.shortcuts import render,  reverse, redirect
from django.views.generic import CreateView
from .forms import ShorteningForm
from .models import Url


class ShorteningView(CreateView):
    model = Url
    template_name = 'homepage.html'
    form_class = ShorteningForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        http_host = self.request.META['HTTP_HOST']
        obj.save()
        Url.assign_shortcode(obj, http_host)
        return redirect(reverse('shortening_result', kwargs={'shortcode': obj.shortcode}))


def url_redirect_view(request, shortcode):
    try:
        obj = Url.objects.get(shortcode=shortcode)
        return HttpResponseRedirect(obj.target_url)
    except Url.DoesNotExist:
        return render(request, '404.html')


def result(request, shortcode):
    url = Url.objects.get(shortcode=shortcode)
    context = {
        'request': request,
        'shortcode': url.full_url,

    }
    return render(request, 'result.html', context)
