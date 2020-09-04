from django.shortcuts import render
from seasonal.const import _get_current_season


def index(request):

    context = {
        'current_season': _get_current_season()
    }

    return render(request, 'frontend/index.html', context)