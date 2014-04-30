#!/usr/bin/env python

# File name: 		projecteuler019.py
# Author: 			Matt McGranaghan
# Date Created:		2014/04/29
# Date Modified: 	2014/04/29
# Python Version: 	2.7

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def solution019():
	target_year = 2001
	month_list_reg = [31,28,31,30,31,30,31,31,30,31,30,31]
	month_list_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

	day_of_week = 2
	day_of_month = 1
	month = 1
	year = 1901
	leap_year = False
	month_list = month_list_reg
	sunday_the_fist = 0

	while year < target_year:

		if (day_of_week == 7) and (day_of_month == 1):
			sunday_the_fist += 1

		day_of_week += 1
		day_of_month += 1

		if day_of_week > 7:
			day_of_week = 1

		if day_of_month > month_list[month-1]:
				day_of_month = 1
				month += 1

		if month > 12:
			year += 1
			month = 1

			if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
				leap_year = True
				month_list = month_list_leap
			else:
				leap_year = False
				month_list =  month_list_reg

	return sunday_the_fist

print solution019()