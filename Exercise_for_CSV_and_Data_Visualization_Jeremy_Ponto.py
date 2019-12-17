# Import the libraries which will be used
import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics

# Open the file
csv_file = open("C:/Users/user/Downloads/20191211100526BN000963572_activity.csv/activity.csv", "r")

# Read the file
csv_reader = csv.reader(csv_file, delimiter = ",")

line = 0
days = {}
intervals = {}
days_list = []
na_counter = 0
days_without_na = {}
weekly_counter = 1
weekdays = {}
weekdays_list = []
weekends = {}
weekends_list = []
for row in csv_reader:
    if line == 0:
        line += 1
    else:
        steps = row[0]
        day = row[1]
        interval = row[2]
        # A 1 : Calculate steps per day for each interval
        if day in days:
            if steps == "NA":
                pass
            else:
                days[day].append(int(steps))
        else:
            if steps == "NA":
                days[day] = [0]
            else:
                days[day] = [int(steps)]
        # B 1 : Total number of steps taken for each interval across all days
        if interval in intervals:
            if steps == "NA":
                pass
            else:
                intervals[interval] += int(steps)
        else:
            if steps == "NA":
                intervals[interval] = 0
            else:
                intervals[interval] = int(steps)
        if day not in days_list:
            days_list.append(day)
        # C 3 : Dataset without missing values for each interval
        if day in days_without_na:
            if steps == "NA":   
                # C 1 : Calculate total number of rows with missing values
                na_counter += 1
                # C 2 : Strategy for filling in the missing values
                days_without_na[day].append(0)
            else:
                days_without_na[day].append(int(steps))
        else:
            if steps == "NA":
                # C 1 : Calculate total number of rows with missing values
                na_counter += 1
                # C 2 : Strategy for filling in the missing values
                days_without_na[day] = [0]
            else:
                days_without_na[day] = [int(steps)]
        # D 1 : Total number of steps taken for each interval across weekdays and weekends
        if weekly_counter <= 5:
            if interval in weekdays:
                if steps == "NA":
                    pass
                else:
                    weekdays[interval] += int(steps)
            else:
                if steps == "NA":
                    weekdays[interval] = 0
                else:
                    weekdays[interval] = int(steps)
            if day not in weekdays_list:
                weekdays_list.append(day)
        elif weekly_counter <= 7:
            if interval in weekends:
                if steps == "NA":
                    pass
                else:
                    weekends[interval] += int(steps)
            else:
                if steps == "NA":
                    weekends[interval] = 0
                else:
                    weekends[interval] = int(steps)
            if day not in weekends_list:
                weekends_list.append(day)
        weekly_counter += 1
        if weekly_counter == 7:
            weekly_counter = 1
        
# A 1 : Calculate total steps per day
print(days)
total_steps_per_day = {}
for day in days:
    total = 0
    for steps in days[day]:
        total += steps
    total_steps_per_day[day] = total
print(total_steps_per_day)

# B 1 : Average number of steps taken for each interval across all days
print(intervals)
print(days_list)
average_intervals = {}
for interval in intervals:
    average_intervals[interval] = intervals[interval] / len(days_list)
print(average_intervals)

# C 1 : Report total number of rows with missing values
print(na_counter)

# C 3 : Dataset without missing values
print(days_without_na)
total_steps_per_day_without_na = {}
for day in days_without_na:
    total = 0
    for steps in days_without_na[day]:
        total += steps
    total_steps_per_day_without_na[day] = total
print(total_steps_per_day_without_na)

# D 1 : Average number of steps taken for each interval across weekdays and weekends
print(weekdays)
print(weekdays_list)
average_weekday_intervals = {}
for interval in weekdays:
    average_weekday_intervals[interval] = weekdays[interval] / len(weekdays_list)
print(average_weekday_intervals)
print(weekends)
print(weekends_list)
average_weekend_intervals = {}
for interval in weekends:
    average_weekend_intervals[interval] = weekends[interval] / len(weekends_list)
print(average_weekend_intervals)

# A 2 : Histogram of total steps per day
plt.bar(total_steps_per_day.keys(), total_steps_per_day.values(), 1.0)
plt.show()

# B 1 : Time series plot of the 5-minute interval and the average number of steps taken averaged across all days
intervals = []
average_steps = []
for interval in average_intervals:
    intervals.append(interval)
for steps in average_intervals.values():
    average_steps.append(steps)
plt.plot(intervals, average_steps)
plt.show()

# B 2 : The maximum average of steps is 202.35185185185185 in the "835" interval.

# C 4 : Histogram of total steps per day without missing values
plt.bar(total_steps_per_day_without_na.keys(), total_steps_per_day_without_na.values(), 1.0)
plt.show()

# D 2 : Time series plot of the 5-minute interval and the average number of steps taken averaged across weekdays and weekends
weekday_intervals = []
average_weekday_steps = []
for interval in average_weekday_intervals:
    weekday_intervals.append(interval)
for steps in average_weekday_intervals.values():
    average_weekday_steps.append(steps)
plt.plot(weekday_intervals, average_weekday_steps)
plt.show()
weekend_intervals = []
average_weekend_steps = []
for interval in average_weekend_intervals:
    weekend_intervals.append(interval)
for steps in average_weekend_intervals.values():
    average_weekend_steps.append(steps)
plt.plot(weekend_intervals, average_weekend_steps)
plt.show()

# A 3 : Mean and median of steps in each day
for day in days:
    print(day, ":")
    print(statistics.mean(days[day]))
    print(statistics.median(days[day]))

# C 4 : Mean and median of steps in each day without missing values
for day in days_without_na:
    print(day, ":")
    print(statistics.mean(days_without_na[day]))
    print(statistics.median(days_without_na[day]))