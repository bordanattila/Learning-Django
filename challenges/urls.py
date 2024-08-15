from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.month_as_a_number),
    path("<str:month>", views.monthly_challenge, name="month_challenge"),
]
