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
        past_run_treadmill_label.append(str(past_dict[i]['treadmill_flagged']))

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
        current_run_treadmill_label.append(str(dict_2[i]['treadmill_flagged']))

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

def MTD(months_ago):
    month_total_dict = calc.monthly_daily_totals(master_dict,months_ago,'distance_miles')
    return latest_value = month_total_dict[max(month_total_dict.keys())] #finds highest date, uses that date to find value


# starts gui
v = ui.load_view()
v.background_color = "black"

button1 = v['segmentedcontrol1']
button1.action = button_action_1

v.present(style='sheet', hide_title_bar=True)

current_period(master_dict)
period(master_dict,0,1)


label41= v['label41']
label41.text = str(MTD(0))
