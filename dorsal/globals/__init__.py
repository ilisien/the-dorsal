import zoneinfo
from django.conf import settings
from django.utils import timezone
from collections import namedtuple

TIME_ZONE = settings.TIME_ZONE #maybe there could be a selector for timezone in the future

class Periods:
    NO_SCHOOL = "Not in session"
    BREAKFAST = "Breakfast"
    PER1 = "Homeroom"
    PER2 = "2nd Period"
    PER3 = "3rd Period"
    PER4 = "Lunch/Activity"
    WPER4 = "Lunch/Advisory"
    PER5 = "5th Period"
    PER6 = "6th Period"

class Schedules:
    WEEKEND = 0
    REGULAR = 1
    WEDNESDAY = 2
    DELAYED = 3

Nav = namedtuple("Nav",("str","path"))

def get_period(datetime,schedule=None):
    time = datetime.strftime("%H:%M")

    if schedule == None:
        if datetime.weekday() == 2:
            schedule = Schedules.WEDNESDAY
        elif datetime.weekday() in [5,6]:
            schedule = Schedules.WEEKEND
            period = Periods.NO_SCHOOL
        else:
            schedule = Schedules.REGULAR

    if schedule == Schedules.REGULAR:
        if '06:50' <= time and time < '07:10':
            period = Periods.BREAKFAST
        elif '07:10' <= time and time < '07:18':
            period = Periods.PER1
        elif '07:18' <= time and time < '08:38':
            period = Periods.PER2
        elif '08:38' <= time and time < '10:03':
            period = Periods.PER3
        elif '10:03' <= time and time < '11:25':
            period = Periods.PER4
        elif '11:25' <= time and time < '12:50':
            period = Periods.PER5
        elif '12:50' <= time and time < '14:15':
            period = Periods.PER6
        else:
            period = Periods.NO_SCHOOL

    elif schedule == Schedules.WEDNESDAY:
        if '06:50' <= time and time < '07:10':
            period = Periods.BREAKFAST
        elif '07:10' <= time and time < '07:18':
            period = Periods.PER1
        elif '07:18' <= time and time < '08:21':
            period = Periods.PER2
        elif '08:21' <= time and time < '09:29':
            period = Periods.PER3
        elif '09:29' <= time and time < '10:37':
            period = Periods.PER5
        elif '10:37' <= time and time < '12:08':
            period = Periods.WPER4
        elif '12:08' <= time and time < '13:15':
            period = Periods.PER6
        else:
            period = Periods.NO_SCHOOL

    elif schedule == Schedules.DELAYED:
        if '08:50' <= time and time < '09:10':
            period = Periods.BREAKFAST
        elif '09:10' <= time and time < '09:18':
            period = Periods.PER1
        elif '09:18' <= time and time < '10:08':
            period = Periods.PER2
        elif '10:08' <= time and time < '11:03':
            period = Periods.PER3
        elif '11:03' <= time and time < '12:25':
            period = Periods.PER4
        elif '12:25' <= time and time < '13:20':
            period = Periods.PER5
        elif '13:20' <= time and time < '14:15':
            period = Periods.PER6
        else:
            period = Periods.NO_SCHOOL

    return period

def get_global_context():
    datetime = timezone.now()
    period = get_period(datetime)
    navlinks = [
        Nav("at scitech","/sections/scitech/"),
        Nav("in pittsburgh","/sections/pittsburgh/"),
        #Nav("politics","/politics/"),
        Nav("technology","/sections/tech/"),
        #Nav("sports","/sports/"),
        Nav("pop culture","/sections/pop/"),
        Nav("editorial","/sections/editorials/")
        #Nav("photography","/photos/"),
        #Nav("open data","/open-data/"),
    ]

    context = {
        'datetime':datetime,
        'period':period,
        'navlinks':navlinks,
    }
    return context