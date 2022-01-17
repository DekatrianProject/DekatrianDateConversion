# -*- coding: utf-8 -*-
"""
Some functions to convert between Dekatrian and Gregorian calendar.
@author: Pena
11\10\2017
dekatrian.com
"""

import calendar


def dek_to_week(dek_day: int, dek_month: int, dek_year: int) -> int:
    """Returns the Gregorian week day from a Dekatrian date.

    Args:
        dek_day (int): Day of the month.
        dek_month (int): Month of the year.
        dek_year (int): Year.

    Return:
        int: The week day.
        Example: 1 = Sunday; 2 = Monday; 3 = Tuesday ... 7 = Saturday.
    """
    week_day = (
        (week_day_on_first_auroran(dek_year) + dekatrian_week(dek_day, dek_month) - 2)
        % 7
    ) + 1
    if dek_month == 0:
        week_day = ((week_day - 3 + dek_day) % 7) + 1
    return week_day


def dekatrian_week(dek_day: int, dek_month: int) -> int:
    """Returns the Dekatrian week day from a Dekatrian date.
    Here we can see the elegance of Dekatrian, since it's not necessary to
    inform the year. Actually, barely it's necessary to inform the month,
    as it's only needed to check if that is an Achronian day.

    Args:
        dek_day (int): Day of the month.
        dek_month (int): Month of the year.

    Return:
        int: The week day.
        Example: 0 = Achronian; 1 = first week day; 2 = second week day ... 7 = seventh.
    """
    if dek_month == 0:
        return 0
    else:
        dek_week_day = ((dek_day - 1) % 7) + 1
        return dek_week_day


def week_day_on_first_auroran(dek_year: int) -> int:
    """Returns the Gregorian week day for the first Auroran of a given year

    Args:
        dek_year (int): Year.

    Return:
        int: The week day.
        Example: 1 = Sunday; 2 = Monday; 3 = Tuesday ... 7 = Saturday.
    """
    week_day = (
        (1 + 5 * ((dek_year) % 4) + 4 * ((dek_year) % 100) + 6 * ((dek_year) % 400)) % 7
    ) + 1
    return week_day


def year_day_on_deka_date(dek_day: int, dek_month: int, dek_year: int) -> int:
    """Returns the day of the year from a Dekatrian date.
    Achronian is the day 1.
    Sinchronian is day 2 when it exists.

    Args:
        dek_day (int): Day of the month.
        dek_month (int): Month of the year.
        dek_year (int): Year.

    Return:
        int: The day of the year.
    """
    if dek_month == 0:
        return dek_day
    else:
        return (calendar.isleap(dek_year)) + 1 + (dek_month - 1) * 28 + dek_day


def year_day_on_greg_date(day: int, month: int, year: int) -> int:
    """Returns the day of the year from a Gregorian date.
    Example1: Jan 1 is the day 1;
    Dez 31 is the day 365 or 366, whether it's a leap year or not

    Args:
        day (int): Day of the month. Example: Jan 1 is the day 1.
        month (int): Month of the year.
        year (int): Year.

    Return:
        int: The day of the year.
    """
    JAN = 31
    FEB = 28 + calendar.isleap(year)
    MAR = 31
    APR = 30
    MAY = 31
    JUN = 30
    JUL = 31
    AUG = 31
    SEP = 30
    OCT = 31
    NOV = 30
    DEC = 31
    gregorian_calendar_months = (
        JAN,
        FEB,
        MAR,
        APR,
        MAY,
        JUN,
        JUL,
        AUG,
        SEP,
        OCT,
        NOV,
        DEC,
    )  # TODO: MUDAR PRA DICIONARIO
    i = 0
    days = 0
    while i < (month - 1):
        days += gregorian_calendar_months[i]
        i += 1
    return days + day


def dek_to_greg(dek_day: int, dek_month: int, dek_year: int) -> tuple:
    """Returns a Gregorian date from a Dekatrian date.

    Args:
        dek_day (int): Day of the month.
        dek_month (int): Month of the year.
        dek_year (int): Year.

    Return:
        tuple: A tuple with the day, month and year.
    """
    year_day = year_day_on_greg_date(dek_day, dek_month, dek_year)
    JAN = 31
    FEB = 28 + calendar.isleap(dek_year)
    MAR = 31
    APR = 30
    MAY = 31
    JUN = 30
    JUL = 31
    AUG = 31
    SEP = 30
    OCT = 31
    NOV = 30
    DEC = 31
    gregorian_calendar_months = (
        JAN,
        FEB,
        MAR,
        APR,
        MAY,
        JUN,
        JUL,
        AUG,
        SEP,
        OCT,
        NOV,
        DEC,
    )  # TODO: MUDAR PRA DICIONARIO
    for month, days in enumerate(gregorian_calendar_months, start=1):
        if year_day > days:
            year_day -= days
        else:
            break
    return (year_day, month, dek_year)


def greg_to_dek(day: int, month: int, year: int) -> tuple:
    """Returns a Dekatrian date from a Gregorian date

    Args:
        day (int): Day of the month.
        month (int): Month of the year.
        year (int): Year.

    Return:
        tuple: A tuple with the day, month and year.
    """
    year_day = year_day_on_greg_date(day, month, year)
    if year_day > (1 + calendar.isleap(year)):
        year_day -= 1 + calendar.isleap(year)
        dek_month = int((year_day - 1) / 28) + 1
        dek_day = (year_day - 1) % 28 + 1
    else:
        dek_month = 0
        dek_day = day
    return (dek_day, dek_month, year)


if __name__ == "__main__":
    # Examples #
    print(
        "Dekatrian 28\\13\\2015 falls on Greg week day: " + str(dek_to_week(28, 13, 2015))
    )
    print("Dekatrian 1\\0\\2016 falls on Greg week day: " + str(dek_to_week(1, 0, 2016)))
    print("Dekatrian 2\\0\\2016 falls on Greg week day: " + str(dek_to_week(2, 0, 2016)))
    print("Dekatrian 1\\1\\2016 falls on Greg week day: " + str(dek_to_week(1, 1, 2016)))
    print("Achronian corresponds to Dekatrian week day: " + str(dekatrian_week(1, 0)))
    print(
        "Dekatrian 1\\1\\2016 happens on Gregorian week day: "
        + str(week_day_on_first_auroran(2016))
    )
    print("Dekatrian 3\\1\\2017 is the year day: " + str(year_day_on_deka_date(3, 1, 2017)))
    print(
        "Dekatrian 10\\10\\2017 corresponds to Gregorian " + str(dek_to_greg(10, 10, 2017))
    )
    print(
        "Gregorian 29/12/2016 is the year day: " + str(year_day_on_greg_date(29, 12, 2016))
    )
    print("Gregorian 3/1/2016 corresponds to Dekatrian: " + str(greg_to_dek(3, 1, 2016)))
