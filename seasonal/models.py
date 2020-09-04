from django.db import models
from .const import (
    SEASON_NAMES,
    SEASON_NUMBER_MAP,
    SEASON_DATES_MAP,
    PRODUCE_CATEGORIES,
    USDA_BASE_URL,
    _convert_to_date
)


class Season(models.Model):
    order = models.IntegerField(unique=True)
    name = models.CharField(unique=True, choices=SEASON_NAMES, max_length=255)
    start_day = models.DateField()
    end_day = models.DateField()

    def save(self, *args, **kwargs):
        self.order = SEASON_NUMBER_MAP.get(self.name, 0)
        self.start_day = _convert_to_date(self.name, 0)
        self.end_day = _convert_to_date(self.name, 1)
        super().save(*args, **kwargs)


class Produce(models.Model):
    name = models.CharField(max_length=255)
    sub_names = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField()
    category = models.CharField(choices=PRODUCE_CATEGORIES, max_length=255)
    seasons = models.ManyToManyField(Season)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-').lower()
        super().save(*args, **kwargs)

    @property
    def usda_url(self):
        return USDA_BASE_URL + '/{}'.format(self.slug).lower()