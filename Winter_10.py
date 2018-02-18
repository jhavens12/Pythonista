import ui #used for pythonista
import console #used for pythonista
import get_time
import get_data
import calc
import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
import pylab
from io import BytesIO
from pprint import pprint
import datetime #recently added
import math #recently added

master_dict = get_data.my_filtered_activities()

def period(dictionary,Sunday,Monday):

    dict_1 = dictionary.copy()
    for key in dictionary:
        if key > get_time.LS(Sunday):
            del dict_1[key]
    for key in dictionary:
        if key < get_time.LM(Monday):
            del dict_1[key]

    past_dict_rev = {k: dict_1[k] for k in list(reversed(sorted(dict_1.keys())))}
    past_dict = {k: past_dict_rev[k] for k in list(sorted(past_dict_rev.keys()))}
    past_run_count = calc.activity_count(past_dict)
    past_mile_list = []
    for i in past_dict:
        past_mile_list.append(float(past_dict[i]['distance_miles']))
    past_miles = ("{0:.2f}".format(sum(past_mile_list)))
    past_ten_percent = ("{0:.2f}".format(float(past_miles) * .1))

    past_run_title_label = []
    for i in list(sorted(past_dict)):
        past_run_title_label.append(past_dict[i]['weekday_short_date'])
    past_run_mile_label = []
    for i in list(sorted(past_dict)):
        past_run_mile_label.append(past_dict[i]['distance_miles'])
    past_run_pace_label = []
    for i in list(sorted(past_dict)):
        past_run_pace_label.append(past_dict[i]['pace'])
    past_run_elapsed_label = []
    for i in list(sorted(past_dict)):
        past_run_elapsed_label.append(str(past_dict[i]['elapsed']))
    past_run_treadmill_label = []
    for i in list(sorted(past_dict)):
        past_run_treadmill_label.append(str(past_dict[i]['total_elevation_feet']))

    remaining(past_ten_percent,past_miles)

    label1= v['label1']
    label1.text = (get_time.convert_weekday_full(get_time.LM(Monday)) + " - " + get_time.convert_weekday_full(get_time.LS(Sunday)))

    label2= v['label2']
    label2.text = str(past_miles)

    # label3= v['label3']
    # label3.text = str(past_run_count)

    label4= v['label4']
    label4.text = str(past_ten_percent)

    label5= v['label5']
    label5.text = ("\n".join(past_run_title_label))

    label6= v['label6']
    label6.text = ("\n".join(past_run_mile_label))

    label7= v['label7']
    label7.text = ("\n".join(past_run_pace_label))

    label8= v['label8']
    label8.text = ("\n".join(past_run_elapsed_label))

    label9= v['label9']
    label9.text = ("\n".join(past_run_treadmill_label))

def current_period(dictionary):
    dict_2 = dictionary.copy()
    global current_miles
    global current_week_count
    for key in dictionary:
        if key < get_time.LM(0):
            del dict_2[key]
    current_week_count = calc.activity_count(dict_2)
    mile_list = []
    for i in dict_2:
        mile_list.append(float(dict_2[i]['distance_miles']))
    current_miles = "{0:.2f}".format(sum(mile_list))

    current_run_title_label = []
    for i in list(sorted(dict_2)):
        current_run_title_label.append(dict_2[i]['weekday_short_date'])
    current_run_mile_label = []
    for i in list(sorted(dict_2)):
        current_run_mile_label.append(dict_2[i]['distance_miles'])
    current_run_pace_label = []
    for i in list(sorted(dict_2)):
        current_run_pace_label.append(dict_2[i]['pace'])
    current_run_elapsed_label = []
    for i in list(sorted(dict_2)):
        current_run_elapsed_label.append(str(dict_2[i]['elapsed']))
    current_run_treadmill_label = []
    for i in list(sorted(dict_2)):
        current_run_treadmill_label.append(str(dict_2[i]['total_elevation_feet']))

    label20= v['label20']
    label20.text = (get_time.weekday(get_time.LM(0)) + " " + str(get_time.LM(0).day) + " - " + get_time.weekday(get_time.now()) + " " + str(get_time.now().day))

    # label21= v['label21']
    # label21.text = str(current_week_count)

    label22= v['label22']
    label22.text = str(current_miles)

    label23= v['label23']
    label23.text = ("\n".join(current_run_title_label))

    label24= v['label24']
    label24.text = ("\n".join(current_run_mile_label))

    label25= v['label25']
    label25.text = ("\n".join(current_run_pace_label))

    label26= v['label26']
    label26.text = ("\n".join(current_run_elapsed_label))

    label27= v['label27']
    label27.text = ("\n".join(current_run_treadmill_label))

def remaining(past_ten_percent,past_miles):
    remaining_miles = ("{0:.2f}".format((float(past_ten_percent) + float(past_miles)) - float(current_miles)))

    label40= v['label40']
    label40.text = str(remaining_miles)

#button
def button_action_1(sender):
    if button1.selected_index == 0:
        period(master_dict,0,1)
    if button1.selected_index == 1:
        period(master_dict,1,2)
    if button1.selected_index == 2:
        period(master_dict,2,3)
    elif button1.selected_index == 3:
        period(master_dict,3,4)

def button_action_2(sender):
    if button2.selected_index == 0:
        Monthly(master_dict.copy())
    elif button2.selected_index == 1:
        Yearly(master_dict.copy())

def MTD(dictionary,months_ago): #month to date
    month_total_dict = calc.monthly_daily_totals(dictionary,months_ago,'distance_miles')
    return month_total_dict[max(month_total_dict.keys())] #finds highest date, uses that date to find value

def Monthly(dictionary):
    this_month_full = calc.monthly_daily_totals(master_dict.copy(),0,'distance_miles')
    last_month_full = calc.monthly_daily_totals(master_dict.copy(),1,'distance_miles')
    this_month = MTD(master_dict.copy(),0)
    last_month = MTD(master_dict.copy(),1)
    month_difference = this_month - last_month
    now = datetime.datetime.now()
    past = datetime.datetime(now.year, now.month - (0-1), 1) - (datetime.timedelta(days=1))
    LOM = datetime.datetime(past.year, past.month, past.day, hour=23, minute=59, second=59)
    days_remaining = LOM.day - now.day
    runs_per_week = 3
    runs_remain = math.ceil(days_remaining*(runs_per_week/7))
    monthly_dict = calc.monthly_stats(master_dict.copy())
    max_miles = 0
    for month in monthly_dict:
        if monthly_dict[month]['miles_ran'] > max_miles:
            max_miles = int(monthly_dict[month]['miles_ran'])
            most_miles_month = month

    print("Miles Ran This Month: "+str(this_month))
    print("Runs This Month: "+str(len(this_month_full)))
    print("Miles Ran Last Month: "+str(last_month))
    print("Runs Last Month: "+str(len(last_month_full)))
    print("Days in Month Remaining: "+str(days_remaining))
    print("Last Month vs This Month: "+str("{0:.2f}".format(month_difference)))
    print("Runs Remain in Month ("+str(runs_per_week)+" per week): "+str(runs_remain))
    print()
    print("GOALS")
    print("Goal of 50 Miles per Month: "+ str("{0:.2f}".format(this_month-50)))
    print("MPR to Match 50m Goal: "+ str("{0:.2f}".format((50-this_month)/runs_remain)))
    print("MPR to Match Last Month: "+str("{0:.2f}".format(abs(month_difference/runs_remain))))
    print("Most Mile Month: "+monthly_dict[most_miles_month]['date_human'])
    print("Most Miles Ran in a month: "+str(max_miles))
    print("MPR to Match Highest Month: "+str("{0:.2f}".format((max_miles-this_month)/runs_remain)))

    #LABELS
    label111= v['label111']
    label111.text = str("This Month")

    label112= v['label112']
    label112.text = str("Run Count")

    label113= v['label113']
    label113.text = str("Last Month")

    label114= v['label114']
    label114.text = str("Run Count")

    label115= v['label115']
    label115.text = str("Difference")

    label116= v['label116']
    label116.text = str("Runs Remain")

    #
    #DATA
    label121= v['label121']
    label121.text = str(this_month)

    label122= v['label122']
    label122.text = str(len(this_month_full))

    label123= v['label123']
    label123.text = str(last_month)

    label124= v['label124']
    label124.text = str(len(last_month_full))

    label125= v['label125']
    label125.text = str("{0:.2f}".format(month_difference))

    label126= v['label126']
    label126.text = str(runs_remain)

def Yearly(dictionary):
    #this year
    past = datetime.datetime(now.year, now.month - (0-1), 1) - (datetime.timedelta(days=1))
    LOM = datetime.datetime(past.year, past.month, past.day, hour=23, minute=59, second=59)
    days_remaining = LOM.day - now.day
    runs_per_week = 3

    ytd_dict = master_dict.copy()
    for key in list(ytd_dict):
        if key < get_time.FOY():
            del ytd_dict[key]
    ytd_miles = []
    for run in ytd_dict:
        ytd_miles.append(float(ytd_dict[run]['distance_miles']))
    miles_this_year = sum(ytd_miles)

    #last year
    timestamp = datetime.datetime.now()
    past_ytd_dict = master_dict.copy()
    for key in list(past_ytd_dict):
        if key < get_time.PFOY():
            del past_ytd_dict[key]
        if key > datetime.datetime(timestamp.year - 1, timestamp.month, timestamp.day): #get date this time last year
            del past_ytd_dict[key]
    pytd_miles = []
    for run in past_ytd_dict:
        pytd_miles.append(float(past_ytd_dict[run]['distance_miles']))
    miles_last_year_this_time = sum(pytd_miles)

    goal_2018 = 600
    MPD = goal_2018/365
    day_of_year = LOM.timetuple().tm_yday
    target_miles = MPD*day_of_year
    remaining_ytd_miles = miles_this_year - target_miles

    print()
    print("YEAR TO DATE")
    print("**********")
    print("Miles Ran This Year: "+str(miles_this_year))
    print("Miles Ran Last Year by now: "+str(miles_last_year_this_time))
    print("Miles Behind Last Year: "+str("{0:.2f}".format(miles_this_year-miles_last_year_this_time)))
    print("2018 Goal for today: "+str(("{0:.2f}".format(target_miles))))
    print("Miles Behind YTD Goal: "+str(("{0:.2f}".format(remaining_ytd_miles))))
    #print("MPR to YTD Goal by End of Month: "+str(("{0:.2f}".format(abs(remaining_ytd_miles)/runs_remain))))

    label111= v['label111']
    label111.text = str("YTD Miles")

    label112= v['label112']
    label112.text = str("Last YTD by now")

    label113= v['label113']
    label113.text = str("Behind")

    label114= v['label114']
    label114.text = str("2018 Goal")

    label115= v['label115']
    label115.text = str("Behind")

    label116= v['label116']
    label116.text = str("")

    #

    label121= v['label121']
    label121.text = str(miles_this_year)

    label122= v['label122']
    label122.text = str(miles_last_year_this_time)

    label123= v['label123']
    label123.text = str("{0:.2f}".format(miles_this_year-miles_last_year_this_time))

    label124= v['label124']
    label124.text = str(("{0:.2f}".format(target_miles)))

    label125= v['label125']
    label125.text = str(("{0:.2f}".format(remaining_ytd_miles)))

    label126= v['label126']
    label126.text = str("")

# starts gui
v = ui.load_view()
v.background_color = "black"

button1 = v['segmentedcontrol1']
button1.action = button_action_1

button2 = v['segmentedcontrol2']
button2.action = button_action_2

v.present(style='sheet', hide_title_bar=True)

#initial data presentation
current_period(master_dict)
period(master_dict,0,1)

#####
##NEW DATA`
####

def print_statements(master_dict):
    past = datetime.datetime(now.year, now.month - (0-1), 1) - (datetime.timedelta(days=1))
    LOM = datetime.datetime(past.year, past.month, past.day, hour=23, minute=59, second=59)
    days_remaining = LOM.day - now.day
    runs_per_week = 3
    
    this_month_full = calc.monthly_daily_totals(master_dict.copy(),0,'distance_miles')
    last_month_full = calc.monthly_daily_totals(master_dict.copy(),1,'distance_miles')

    this_month = MTD(master_dict.copy(),0)
    last_month = MTD(master_dict.copy(),1)

    month_difference = this_month - last_month

    now = datetime.datetime.now()
    past = datetime.datetime(now.year, now.month - (0-1), 1) - (datetime.timedelta(days=1))

    days_remaining = LOM.day - now.day
    runs_per_week = 3
    runs_remain = math.ceil(days_remaining*(runs_per_week/7))

    monthly_dict = calc.monthly_stats(master_dict.copy())
    max_miles = 0
    for month in monthly_dict:
        if monthly_dict[month]['miles_ran'] > max_miles:
            max_miles = int(monthly_dict[month]['miles_ran'])
            most_miles_month = month

    print("MONTHLY")
    print("**********")
    print("Miles Ran This Month: "+str(this_month))
    print("Runs This Month: "+str(len(this_month_full)))
    print("Miles Ran Last Month: "+str(last_month))
    print("Runs Last Month: "+str(len(last_month_full)))
    print("Days in Month Remaining: "+str(days_remaining))
    print("Last Month vs This Month: "+str("{0:.2f}".format(month_difference)))
    print("Runs Remain in Month ("+str(runs_per_week)+" per week): "+str(runs_remain))
    print()
    print("GOALS")
    print("Goal of 50 Miles per Month: "+ str("{0:.2f}".format(this_month-50)))
    print("MPR to Match 50m Goal: "+ str("{0:.2f}".format((50-this_month)/runs_remain)))
    print("MPR to Match Last Month: "+str("{0:.2f}".format(abs(month_difference/runs_remain))))
    print("Most Mile Month: "+monthly_dict[most_miles_month]['date_human'])
    print("Most Miles Ran in a month: "+str(max_miles))
    print("MPR to Match Highest Month: "+str("{0:.2f}".format((max_miles-this_month)/runs_remain)))

    weekly_dict = calc.weekly_stats(master_dict.copy())

    max_weekly_miles = 0
    for week in weekly_dict:
        if weekly_dict[week]['miles_ran'] > max_weekly_miles:
            max_weekly_miles = int(weekly_dict[week]['miles_ran'])
            most_miles_week = week

    print()
    print("WEEKLY")
    print("********")
    print("Miles This Week: "+str(current_miles))
    print("Most Mile Week: "+str(weekly_dict[most_miles_week]['date_human']))
    print("Most Miles Run in a Week: "+str(max_weekly_miles))
    print("Miles to Match Highest Week: "+str(float(max_weekly_miles)-float(current_miles)))

    #this year
    ytd_dict = master_dict.copy()
    for key in list(ytd_dict):
        if key < get_time.FOY():
            del ytd_dict[key]
    ytd_miles = []
    for run in ytd_dict:
        ytd_miles.append(float(ytd_dict[run]['distance_miles']))
    miles_this_year = sum(ytd_miles)

    #last year
    timestamp = datetime.datetime.now()
    past_ytd_dict = master_dict.copy()
    for key in list(past_ytd_dict):
        if key < get_time.PFOY():
            del past_ytd_dict[key]
        if key > datetime.datetime(timestamp.year - 1, timestamp.month, timestamp.day): #get date this time last year
            del past_ytd_dict[key]
    pytd_miles = []
    for run in past_ytd_dict:
        pytd_miles.append(float(past_ytd_dict[run]['distance_miles']))
    miles_last_year_this_time = sum(pytd_miles)

    goal_2018 = 600
    MPD = goal_2018/365
    day_of_year = LOM.timetuple().tm_yday
    target_miles = MPD*day_of_year
    remaining_ytd_miles = miles_this_year - target_miles

    print()
    print("YEAR TO DATE")
    print("**********")
    print("Miles Ran This Year: "+str(miles_this_year))
    print("Miles Ran Last Year by now: "+str(miles_last_year_this_time))
    print("Miles Behind Last Year: "+str("{0:.2f}".format(miles_this_year-miles_last_year_this_time)))
    print("2018 Goal for today: "+str(("{0:.2f}".format(target_miles))))
    print("Miles Behind YTD Goal: "+str(("{0:.2f}".format(remaining_ytd_miles))))
    print("MPR to YTD Goal by End of Month: "+str(("{0:.2f}".format(abs(remaining_ytd_miles)/runs_remain))))

print_statements(master_dict.copy())
