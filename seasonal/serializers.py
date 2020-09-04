from rest_framework import serializers
from .models import Season, Produce


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('name',)


class ProduceSerializer(serializers.ModelSerializer):

    usda_url = serializers.ReadOnlyField()

    class Meta:
        model = Produce
        fields = ('name', 'category', 'seasons', 'usda_url')