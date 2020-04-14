from django.urls import path
from . import views


urlpatterns = [

    path('', views.ShorteningView.as_view(), name='homepage_view'),
    path('shorted/<shortcode>', views.result, name='shortening_result'),
    path('<str:shortcode>', views.url_redirect_view, name='check')

]