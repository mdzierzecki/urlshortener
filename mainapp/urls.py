from django.urls import path, re_path
from django.conf.urls import url
from .views import ShorteningView, result, url_redirect_view
from django.contrib import admin


urlpatterns = [

    path('', ShorteningView.as_view(), name='homepage_view'),
    path('shorted/<shortcode>', result, name='shortening_result'),
    path('<str:shortcode>', url_redirect_view, name='check')

]