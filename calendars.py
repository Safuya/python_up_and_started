import calendar


c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2014, 4, 0, 0)
print(str)


# hc = calendar.HTMLCalendar(calendar.MONDAY)
# str = hc.formatmonth(2014, 4)
# print(str)


# for i in c.itermonthdays(2014, 4):
#     print(i)


# for month in calendar.month_name:
#     print(month)


for m in range(1,13):
    cal = calendar.monthcalendar(2014, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
