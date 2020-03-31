from django.urls import path, re_path
from django.conf.urls import url
from .views import ShorteningView, result, url_redirect_view


urlpatterns = [
    path('', ShorteningView.as_view(), name='homepage_view'),
    path('shorted/<shortcode>', result, name='shortening_result'),
    re_path(r'(?P<shortcode>[a-z]+)', url_redirect_view, name='check')

]