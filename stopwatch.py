from tkinter import *
from datetime import datetime

# Temp количество секунд с момента старта секундомера
temp = 0

# After_id Идентификатор возвращаемый методом after
after_id = ''


def tick():
    global temp, after_id

    # 1000 милисекунд это период, когда каждый раз будет вызываться функция tick
    after_id = root.after(1000, tick)

    # datetime.fromtimestamp(temp) возвращает дату, соответствующую количеству секунд прошедших с начала эпохи,
    # а дополнение strftime возвращает форматированную строку
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    time_label.configure(text=str(f_temp))
    temp += 1

def start_sw():
    start_btn.grid_forget()
    stop_btn.grid(row=1, columnspan=2, sticky='ew')
    tick()


def stop_sw():
    stop_btn.grid_forget()
    continue_btn.grid(row=1, column=0, sticky='ew')
    reset_btn.grid(row=1, column=1, sticky='ew')

    root.after_cancel(after_id)

def continue_sw():
    continue_btn.grid_forget()
    reset_btn.grid_forget()
    stop_btn.grid(row=1, columnspan=2, sticky='ew')
    tick()

def reset_sw():
    global temp

    temp = 0
    time_label.configure(text='00:00')
    continue_btn.grid_forget()
    reset_btn.grid_forget()
    start_btn.grid(row=1, columnspan=2, sticky='ew')


root = Tk()

root.title('Stop Watch')

time_label = Label(root, width=5, font=('Ubuntu', 100), text='00:00')
time_label.grid(row=0, columnspan=2)

start_btn = Button(root, text='Start', font=('Ubuntu', 30), command=start_sw)
stop_btn = Button(root, text='Stop', font=('Ubuntu', 30), command=stop_sw)
continue_btn = Button(root, text='Continue', font=('Ubuntu', 30), command=continue_sw)
reset_btn = Button(root, text='Reset', font=('Ubuntu', 30), command=reset_sw)

start_btn.grid(row=1, columnspan=2, sticky='ew')

root.mainloop()
