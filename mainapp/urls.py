from django.urls import path

from .views import ShorteningView, result


urlpatterns = [
    path('', ShorteningView.as_view(), name='homepage_view'),
    path('result/', result, name='shorening_result'),


]