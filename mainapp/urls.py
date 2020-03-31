from django.urls import path
from .views import ShorteningView, result, url_redirect_view


urlpatterns = [

    path('', ShorteningView.as_view(), name='homepage_view'),
    path('shorted/<shortcode>', result, name='shortening_result'),
    path('<str:shortcode>', url_redirect_view, name='check')

]