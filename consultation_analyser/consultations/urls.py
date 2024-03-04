from django.urls import path
from .views import show_question

urlpatterns = [path("questions/<str:slug>", show_question)]