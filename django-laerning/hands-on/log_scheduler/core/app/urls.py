from django.urls import path
from .views import Test

urlpatterns = [
    path('log/', Test.as_view()),
]
