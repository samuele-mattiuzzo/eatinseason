from .const import _get_current_season_number
from .models import Season, Produce
from .serializers import SeasonSerializer, ProduceSerializer
from rest_framework import generics


class SeasonListCreate(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class ProduceListCreate(generics.ListCreateAPIView):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer


class InSeasonListView(generics.ListAPIView):
    serializer_class = ProduceSerializer
    
    def get_queryset(self):
        season = _get_current_season_number()
        return Produce.objects.filter(seasons__order=season).order_by('name')