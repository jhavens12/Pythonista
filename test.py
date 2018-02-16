import datetime
import math
import get_time
import get_data
import calc
from pprint import pprint

master_dict = get_data.my_filtered_activities()

#get dictionary of months and their total miles ran

def MTD(dictionary,months_ago):
    month_total_dict = calc.monthly_daily_totals(dictionary,months_ago,'distance_miles')
    return month_total_dict[max(month_total_dict.keys())] #finds highest date, uses that date to find value

pprint(calc.weekly_stats(master_dict.copy()))
