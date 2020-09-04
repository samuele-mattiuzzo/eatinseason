from datetime import datetime, date

USDA_BASE_URL = 'https://snaped.fns.usda.gov/seasonal-produce-guide'

SEASON1 = 'spring'
SEASON2 = 'summer'
SEASON3 = 'fall'
SEASON4 = 'winter'

SEASON_NAMES = (
    (SEASON1, SEASON1),
    (SEASON2, SEASON2),
    (SEASON3, SEASON3),
    (SEASON4, SEASON4)
)

SEASON_NUMBER_MAP = {
    SEASON1: 1,
    SEASON2: 2,
    SEASON3: 3,
    SEASON4: 4
}

SEASON_DATES_MAP = {
    SEASON1: ('1/3', '31/5'),
    SEASON2: ('1/6', '31/8'),
    SEASON3: ('1/9', '30/11'),
    SEASON4: ('1/12', '29/2')
}

PRODUCE_CATEGORIES = (
    ('fruit', 'fruit'),
    ('vegetable', 'vegetable')
)

# helpers
def _convert_to_date(name, pos):
    return datetime.strptime(
        SEASON_DATES_MAP[name][pos], '%d/%m'
    ).date()

def _get_current_season():
    today = datetime.today()
    today = date(day=today.day, month=today.month, year=1900)

    for season in SEASON_DATES_MAP.keys():
        start = _convert_to_date(season, 0)
        end = _convert_to_date(season, 1)

        if start <= today <= end:
            return season

def _get_current_season_number():
    return SEASON_NUMBER_MAP.get(
        _get_current_season()
    )