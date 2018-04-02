# Learning Alignment Options In UI
# Pythonista
# Flex LRTBWH
import ui

w,h = ui.get_screen_size()
h = h
view = ui.View(bg_color = 'lightyellow', frame = (0,0,w,h))
#view.flex = 'WH'
# label height and button width
bh = 32
bw = 80
# margin

smg = 5
tmg = 20


#view_1 =  ui.View([frame=(0, 0, 50, 50), flex='', background_color=black, name=None])
view_1 =  ui.View(frame=(tmg, smg, w/2, h), background_color='black')

bt1 = ui.Button(name = 'Button1', bg_color ='white', frame = (tmg, smg, bw, bh))
bt1.border_color = 'black'
bt1.tint_color = 'black'
bt1.border_width = 1
bt1.alignment=1
bt1.title = 'BUTTON1'

view_1.add_subview(lb1)


lb1 = ui.Label(name = 'Label1', bg_color = 'yellow', frame =(smg,tmg,bw,bh))
lb1.border_color = 'black'
lb1.border_width = 1
lb1.flex = 'RB'
lb1.alignment=1
lb1.text = lb1.flex

lb2 = ui.Label(name = 'Label2', bg_color = 'yellow', frame =(w-(bw+smg),smg, bw,bh))
lb2.border_color = 'black'
lb2.border_width = 1
lb2.flex = 'LB'
lb2.alignment=1
lb2.text = lb2.flex

lb3 = ui.Label(name = 'Label3', bg_color = 'yellow', frame =(smg,h-(bh+smg),bw,bh))
lb3.border_color = 'black'
lb3.border_width = 1
lb3.flex = 'RT'
lb3.alignment=1
lb3.text = lb3.flex

lb4 = ui.Label(name = 'Label4', bg_color = 'yellow', frame =(w-(bw+smg),h-(bh+smg),bw,bh))
lb4.border_color = 'black'
lb4.border_width = 1
lb4.flex = 'LT'
lb4.alignment=1
lb4.text = lb4.flex

# center
lb5 = ui.Label(name = 'Label5', bg_color = 'yellow', frame =((w-bw)*.5,(h-bh)*.5,bw,bh))
lb5.border_color = 'black'
lb5.border_width = 1
lb5.flex = 'LRTB'
lb5.alignment=1
lb5.text = lb5.flex

view.add_subview(lb1)
view.add_subview(lb2)
view.add_subview(lb3)
view.add_subview(lb4)
view.add_subview(lb5)

#view.present('screen')
view.add_subview(view_1)
view.present(style='sheet', hide_title_bar=True)
