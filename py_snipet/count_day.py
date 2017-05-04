#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   Date    :   17/4/13 上午11:39
#   Desc    :   Python 实现：Count the day of the input date

DAYS_IN_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MINYEAR = 1
MAXYEAR = 9999


def count_days_before_month():
    """
    :return: [None, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    """
    days_before_month_list = [None]
    dbm = 0
    for dim in DAYS_IN_MONTH[1:]:
        days_before_month_list.append(dbm)
        dbm += dim
    return days_before_month_list

DAYS_BEFORE_MONTH = count_days_before_month()


def is_leap(year):
    """
    :param year
    :return: leap year -> 1, else 0
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(year, month):
    """
    :param year
    :param month
    :return: days in that month in that year
    """
    if month == 2 and is_leap(year):
        return 29
    return DAYS_IN_MONTH[month]


def check_date_fields(year, month, day):
    """
    检查 date 的合法性
    """
    if not MINYEAR <= year <= MAXYEAR:
        raise ValueError('year must be in %d..%d' % (MINYEAR, MAXYEAR), year)
    if not 1 <= month <= 12:
        raise ValueError('month must be in 1..12', month)
    dim = days_in_month(year, month)
    if not 1 <= day <= dim:
        raise ValueError('day must be in 1..%d' % dim, day)


def day_of_year(year, month, day):
    check_date_fields(year, month, day)
    return DAYS_BEFORE_MONTH[month] + (month > 2 and is_leap(year)) + day

if __name__ == '__main__':
    assert day_of_year(2016, 1, 1) == 1
    assert day_of_year(2016, 1, 3) == 3
    assert day_of_year(2016, 2, 1) == 32
