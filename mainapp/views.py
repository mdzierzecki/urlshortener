from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import FormView, CreateView
from .forms import ShorteningForm
from .models import Url


class ShorteningView(CreateView):
    model = Url
    template_name = 'homepage.html'
    form_class = ShorteningForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        http_host = self.request.META['HTTP_HOST']
        obj.save(http_host)
        return redirect(reverse('shortening_result', kwargs={'shortcode': obj.shortcode}))


def url_redirect_view(request, shortcode, *args, **kwards):
    obj = get_object_or_404(Url, shortcode=shortcode)
    return HttpResponseRedirect(obj.target_url)


def result(request, shortcode):
    url = Url.objects.get(shortcode=shortcode)
    context = {
        'request': request,
        'shortcode': url.full_url,

    }
    return render(request, 'result.html', context)
