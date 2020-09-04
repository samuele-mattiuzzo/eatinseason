from django.urls import path
from . import views

urlpatterns = [
    path('api/seasons', views.SeasonListCreate.as_view()),
    path('api/produce', views.ProduceListCreate.as_view()),
    path('api/inseason', views.InSeasonListView.as_view())
]