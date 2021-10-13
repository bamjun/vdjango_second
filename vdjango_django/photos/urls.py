from django.urls import path, include
from django.urls.resolvers import URLPattern

from photos import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),



]
