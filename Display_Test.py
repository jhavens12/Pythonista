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
bw = w/2
sp = 5
# margin

smg = 5
tmg = 20

view_1 =  ui.ScrollView(frame=(smg, tmg, w/2, h), background_color='orange')
my_range = list(range(0,5))

view_1.content_size = (w/2,(tmg+sp)*max(my_range)+bh+sp)

def refresh(sender):
    view_1.remove_subview(sender)

for n in my_range:
    button_name = "bt"+str(n)
    btn_tmg = (tmg+sp)*n
    button_name = ui.Button(name = button_name, bg_color ='white', frame = (0, btn_tmg, bw, bh))
    button_name.border_color = 'black'
    button_name.tint_color = 'black'
    button_name.border_width = 1
    button_name.alignment=1
    button_name.title = "bt"+str(n)
    button_name.action = refresh

    view_1.add_subview(button_name)


#view.present('screen')
view.add_subview(view_1)
view.present(style='sheet', hide_title_bar=True)
