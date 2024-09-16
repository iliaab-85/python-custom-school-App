from jdatetime import datetime as jdatetime
import jdatetime

def dates():

    from datetime import datetime, timedelta
    from jdatetime import datetime as jdatetime
    import persian
    yesterday = datetime.now() - timedelta(0)

    jdate_yesterday = jdatetime.fromgregorian(day=yesterday.day, month=yesterday.month,
                                              year=yesterday.year).strftime("%Y/%m/%d")
    jdate_yesterday_persian = persian.convert_en_numbers(jdate_yesterday)

    return jdate_yesterday_persian


def days():
    from jdatetime import datetime as jdatetime
    today = jdatetime.now()
    day_of_week = today.strftime("%A")

    day_of_week_persian = {
        "Saturday": "شنبه",
        "Sunday": "یکشنبه",
        "Monday": "دوشنبه",
        "Tuesday": "سه‌شنبه",
        "Wednesday": "چهارشنبه",
        "Thursday": "پنجشنبه",
        "Friday": "جمعه"
    }[day_of_week]
    return day_of_week_persian

def months():
    now = jdatetime.date.today()

    month_names = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان",
                   "آذر", "دی", "بهمن","اسفند"]

    return month_names[now.month - 1]

def get_month(Value):
    now = jdatetime.date.today()

    month_names = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان",
                   "آذر", "دی", "بهمن","اسفند"]

    return month_names[now.month - 1]


def get_season():
    import datetime
    now = datetime.datetime.now()
    month = now.month
    if month in [12, 1, 2]:
        return "زمستان"
    elif month in [3, 4, 5]:
        return "بهار"
    elif month in [6, 7, 8]:
        return "تابستان"
    else:
        return "پاییز"

def Full_Date():
    from jdatetime import date
    import persian
    months_fa = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    today = date.today()
    day = days()
    FullDate = f"{day} {today.day} {months_fa[today.month - 1]} {today.year}"
    p_FullDate = persian.convert_en_numbers(FullDate)

    return p_FullDate

def lasts_day(days):
    import datetime
    from jdatetime import datetime as jdatetime
    import persian

    persian_days = {
        5: "شنبه",
        6: "یکشنبه",
        0: "دوشنبه",
        1: "سه‌شنبه",
        2: "چهارشنبه",
        3: "پنجشنبه",
        4: "جمعه"
    }

    persian_months = {
        1: "فروردین",
        2: "اردیبهشت",
        3: "خرداد",
        4: "تیر",
        5: "مرداد",
        6: "شهریور",
        7: "مهر",
        8: "آبان",
        9: "آذر",
        10: "دی",
        11: "بهمن",
        12: "اسفند"
    }
    dates = []
    today = datetime.date.today()
    days += 1
    for i in range(days):
        persian_date = jdatetime.fromgregorian(day=today.day, month=today.month, year=today.year)
        persian_day_name = persian_days[today.weekday()]
        persian_month_name = persian_months[persian_date.month]
        dates.append(persian.convert_en_numbers(f"{persian_day_name} {persian_date.day} {persian_month_name} {persian_date.year}"))
        today -= datetime.timedelta(days=1)
    return dates

def find_date(year, month, day):
    from jdatetime import datetime as jdatetime
    jalali_date = jdatetime(year, month, day)
    gregorian_date = jalali_date.togregorian()
    day_of_week = gregorian_date.strftime("%A")
    day_of_week_persian = {
            "Saturday": "شنبه",
            "Sunday": "یکشنبه",
            "Monday": "دوشنبه",
            "Tuesday": "سه‌شنبه",
            "Wednesday": "چهارشنبه",
            "Thursday": "پنجشنبه",
            "Friday": "جمعه"
        }[day_of_week]
    persian_months = {
            1: "فروردین",
            2: "اردیبهشت",
            3: "خرداد",
            4: "تیر",
            5: "مرداد",
            6: "شهریور",
            7: "مهر",
            8: "آبان",
            9: "آذر",
            10: "دی",
            11: "بهمن",
            12: "اسفند"
        }
    monthss = persian_months[month]
    return f"{day_of_week_persian} {day} {monthss} {year}"

def baze_date(startyear, startmonth, startday, endyear, endmonth, endday):
    from jdatetime import datetime as jdatetime, timedelta

    start_date = jdatetime(startyear, startmonth, startday)
    end_date = jdatetime(endyear, endmonth, endday)

    persian_days = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
    persian_months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن",
                      "اسفند"]

    dates = []
    List = []
    while start_date >= end_date:
        dates.append(start_date)
        start_date -= timedelta(days=1)

    for date in dates:
        List.append(f"{persian_days[date.weekday()]} {date.day} {persian_months[date.month - 1]} {date.year}")

    if List == []:
        start_date = jdatetime(endyear, endmonth, endday)
        end_date = jdatetime(startyear, startmonth, startday)

        persian_days = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
        persian_months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن",
                          "اسفند"]

        dates = []
        List = []
        while start_date >= end_date:
            dates.append(start_date)
            start_date -= timedelta(days=1)

        for date in dates:
            List.append(f"{persian_days[date.weekday()]} {date.day} {persian_months[date.month - 1]} {date.year}")
        print(len(List))
        return List

    else:
        print(len(List))
        return List