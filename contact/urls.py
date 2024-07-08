from django.urls import path
from .views import *
urlpatterns = [
    path('info', ContactInfoView.as_view(), name='contact-info'),
    path('', ContactView.as_view(), name='contact'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]