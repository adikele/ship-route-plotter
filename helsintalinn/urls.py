from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('bargraphs/', views.select_country_form, name='country_form'),  #for bargraphs -- adding 25 Monday
]