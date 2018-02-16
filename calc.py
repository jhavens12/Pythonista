#v1.2
#This is the main file unless I made a mistake
import time
import datetime
from datetime import date
import get_time
import pprint


#
def activity_count(dictionary):
    #counts amount of keys in dictionary
    amount = len(dictionary.keys())
    amount_str = str(amount)
    return amount_str
#

#New:

def full_running_totals(dictionary1,days,unit):
    #creadted for use with master_dict
    #newest and working
    #limit days after this calculation for range
    #Creates running totals for each day - not just activity day
    calculation_range_time = []
    final_list = []
    dictionary = dictionary1.copy()
    x = days
    #time functions
    now = datetime.datetime.now()
    start_of_today = datetime.datetime(now.year, now.month, now.day, hour=0, minute=0, second=0)
    end_of_today = datetime.datetime(now.year, now.month, now.day, hour=23, minute=59, second=59)

    difference = start_of_today - get_time.forever() #fix start peroid

    calculation_range = list(range(0,(difference.days +1))) #creates list from past date(given) to current date
    calculation_range_rev = list(reversed(calculation_range))
    calculation_range_time = [end_of_today - datetime.timedelta(days=x) for x in range(0,(difference.days +1))]

    for i,f in zip(calculation_range_time,calculation_range): #for every calculation day ex 1,2,3,4,5 back
        dictionary_1 = dictionary.copy() #create a new dictionary
        oldest_time = end_of_today - (datetime.timedelta(days=(x+f)))
        for key in list(dictionary_1):
            if key > i:
                del dictionary_1[key] #delete keys newer than calculation day
        for key in list(dictionary_1):
            if key < oldest_time: #delete keys older than oldest time
                 del dictionary_1[key]
        value_list = []
        for key in dictionary_1:
            value_list.append(float(dictionary_1[key][unit])) #adds variables to list
        list_sum = sum(value_list)
        final_list.append(list_sum)
    new_date_list = []
    for i in calculation_range: #create list of days going backwards from today
        new_day = get_time.day(i)
        new_date_list.append(new_day)
    new_dict = dict(zip(new_date_list, final_list))
    return new_dict

def monthly_daily_totals(dictionary,time_input,unit_input):
    #for use with masterdict (get_data.my_filtered_activities())
    #01.29.18
    #takes in number for how many months ago. Ex 0 is current, 1 is last month
    x_list = []
    y_list = []

    #filters out only dates needed
    for key in list(dictionary):
        if key < get_time.FOM(time_input): #if older than first of month
            del dictionary[key]
    for key in list(dictionary):
       if key > get_time.LOM(time_input): #if newer than first of month
           del dictionary[key]

    calculation_day_count = (get_time.LOM(time_input) - get_time.FOM(time_input)).days #how many days in the month
    calculation_day_range = list(range(1,calculation_day_count+2)) #range of 1 to the days in the month - calculation days

    mile_count = 0
    mile_count_list = [] #list of miles
    day_count_list = [] #list of days miles occurred
    for day in calculation_day_range:  #ex 1-31
        for activity in dictionary:
            if activity.day == day: #if the day of the activity matches the day in the list
                mile_count = mile_count + float(dictionary[activity][unit_input])
                mile_count_list.append(mile_count) #add mile count
                day_count_list.append(activity.day) #add day that count occurs

    return dict(zip(day_count_list,mile_count_list))
