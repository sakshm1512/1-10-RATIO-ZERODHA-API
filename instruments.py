import datetime
from dateutil.relativedelta import relativedelta, TH, WE
import calendar

def tsym_atm(names, strikes, atm):
    if names == 1:
        name = 'BANKNIFTY'
        wk = 2
    if names == 0:
        name = 'NIFTY'
        wk = 3

    listString = []

    todayte = datetime.datetime.now().date()
    # todayte = datetime.datetime(2023, 9, 28)

    days_until_thursday = (wk - todayte.weekday() + 7) % 7

    # Add the calculated number of days to the current date to get the next Thursday
    t = todayte + datetime.timedelta(days=days_until_thursday)

    thursday_day = t.strftime("%d")
    thursday_month = t.month

    # Check if the Thursday is the last Thursday of the month
    next_thursday = t + relativedelta(weeks=1)
    if next_thursday.month != thursday_month:
        thursday_month = calendar.month_abbr[t.month]
        formatstring = f"NFO:{name}{t.strftime('%y')}{str.upper(thursday_month)}"
    else:
        formatstring = f"NFO:{name}{t.strftime('%y')}{thursday_month}{thursday_day}"

    for x in strikes:
        if x > atm:
            suffix = 'CE'
        if x < atm:
            suffix = 'PE'

        
        listString.append(formatstring + str(x) + suffix)

    return listString


def tsym_all(names, strikes):
    if names == 1:
        name = 'BANKNIFTY'
        wk = 2
    if names == 0:
        name = 'NIFTY'
        wk = 3

    listString = []

    todayte = datetime.datetime.now().date()
    # todayte = datetime.datetime(2023, 9, 21)

    days_until_thursday = (wk - todayte.weekday() + 7) % 7

    # Add the calculated number of days to the current date to get the next Thursday
    t = todayte + datetime.timedelta(days=days_until_thursday)

    thursday_day = t.strftime("%d")
    thursday_month = t.month

    # Check if the Thursday is the last Thursday of the month
    next_thursday = t + relativedelta(weeks=1)
    if next_thursday.month != thursday_month:
        thursday_month = calendar.month_abbr[t.month]
        formatstring = f"NFO:{name}{t.strftime('%y')}{str.upper(thursday_month)}"
    else:
        formatstring = f"NFO:{name}{t.strftime('%y')}{thursday_month}{thursday_day}"

    suffix = 'CE'
  
    suffix2 = 'PE'

    for x in strikes:

        listString.append(formatstring + str(x) + suffix)
        listString.append(formatstring + str(x) + suffix2)

    return listString


def findtoken(name):
    names = name
    todayte = datetime.datetime.now().date()
    # todayte = datetime.datetime(2023, 9, 29)
    cmon = todayte.month

    # Find the last Thursday of the current month
    for i in range(1, 6):
        t = todayte + relativedelta(weekday=TH(i))
        if t.month != cmon:
            # since t is exceeded we need the last one, which we can get by subtracting -2 since it is already a Thursday.
            t = t + relativedelta(weekday=TH(-2))
            break


    if todayte > t:
        # Move to the next month
        t = t + relativedelta(months=1)

    zdha = []

    currentyear = t.strftime("%y")
    currentMonth = calendar.month_abbr[t.month]

    # Generate the strings for the current month
    for i in range(len(names)):
        zdha.append('NFO:' + names[i] + currentyear + str.upper(currentMonth) + "FUT")

    return zdha


def tsym_BN_CE(strikes):

    name = 'BANKNIFTY'
    wk = 2

    listString = []

    todayte = datetime.datetime.now().date()
    # todayte = datetime.datetime(2023, 9, 28)

    days_until_thursday = (wk - todayte.weekday() + 7) % 7

    # Add the calculated number of days to the current date to get the next Thursday
    t = todayte + datetime.timedelta(days=days_until_thursday)

    thursday_day = t.strftime("%d")
    thursday_month = t.month

    # Check if the Thursday is the last Thursday of the month
    next_thursday = t + relativedelta(weeks=1)
    if next_thursday.month != thursday_month:
        thursday_month = calendar.month_abbr[t.month]
        formatstring = f"NFO:{name}{t.strftime('%y')}{str.upper(thursday_month)}"
    else:
        formatstring = f"NFO:{name}{t.strftime('%y')}{thursday_month}{thursday_day}"

    for x in strikes:

        suffix = 'CE'
        listString.append(formatstring + str(x) + suffix)

    return listString
