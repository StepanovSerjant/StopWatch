from tkinter import *
from tkinter import messagebox
from datetime import datetime

"""
В графических приложениях мы не можем использовать бесконечные циклы, потому что графические приложение
один большой цикл обработки событий и мы не можем запускать в нем другие бесконечные циклы. Это приведет
к зависанию интерфейса. В нашем случае бесконечный цикл это сам секундомер. 
"""

# Temp количество секунд с момента старта секундомера
temp = 0

# After_id Идентификатор возвращаемый методом after
after_id = ''

# Счетчик кругов
count_lap = 0

# Запись данных секундомера для расчета кругов
watch_sec = ''


def raschet(a, b):
    chislo = datetime.strptime(a, "%M:%S")
    chislo2 = datetime.strptime(b, "%M:%S")

    result = str(chislo - chislo2)[2:]

    return result


def tick():
    global temp, after_id

    # 1000 милисекунд это период, когда каждый раз будет вызываться функция tick
    after_id = root.after(1000, tick)

    # datetime.fromtimestamp(temp) возвращает дату, соответствующую количеству секунд прошедших с начала эпохи,
    # а дополнение strftime возвращает форматированную строку
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    watch_lbl.configure(text=str(f_temp))
    temp += 1

def start_sw():
    start_btn.grid_forget()

    stop_btn.grid(row=1, column=0, sticky='ew')
    lap_btn.grid( row=1, column=1, sticky='ew' )
    
    tick()

def lap():
    global count_lap, watch_sec

    count_lap += 1

    if count_lap < 2:
        lap_lbl = Label(root, width=5, font=('Ubuntu', 45), bg='green')
        lap_lbl.configure(text=watch_lbl.cget('text'))
        lap_lbl.grid( row=3 + count_lap, columnspan=2, sticky='ew')
        clear_btn.grid(row=3, columnspan=2, sticky='ew')
        watch_sec = lap_lbl.cget('text')
    else:
        if count_lap > 5:
            messagebox.showinfo("Sorry :(","Max number of laps")
        else:
            if count_lap % 2 == 0:
                lap_lbl = Label(root, width=5, font=('Ubuntu', 45), bg='red')
            else:
                lap_lbl = Label(root, width=5, font=('Ubuntu', 45), bg='green')

            lap_lbl.configure(text=raschet(watch_lbl.cget('text'), watch_sec))
            lap_lbl.grid( row=3 + count_lap, columnspan=2, sticky='ew')
            clear_btn.grid(row=3, columnspan=2, sticky='ew')

            watch_sec = lap_lbl.cget('text')


def stop_sw():

    stop_btn.grid_forget()

    reset_btn.grid(row=1, columnspan=2, sticky='ew')
    continue_btn.grid(row=2, column=0, sticky='ew')
    lap_btn.grid(row=2, column=1, sticky='ew')

    root.after_cancel(after_id)

def continue_sw():
    continue_btn.grid_forget()
    reset_btn.grid_forget()

    stop_btn.grid(row=1, column=0, sticky='ew')
    lap_btn.grid(row=1, column=1, sticky='ew')

    tick()

def reset_sw():
    global temp

    continue_btn.grid_forget()
    reset_btn.grid_forget()
    lap_btn.grid_forget()

    temp = 0
    watch_lbl.configure(text='00:00')
    start_btn.grid(row=1, columnspan=2, sticky='ew')


def clear():
    global count_lap

    count_lap = 0

    lst = root.grid_slaves()

    for l in lst:
        if 'label' in l.winfo_name():
            l.grid_forget()

    clear_btn.grid_forget()
    stop_btn.grid_forget()
    lap_btn.grid_forget()
    continue_btn.grid_forget()

    watch_lbl.grid(row=0, columnspan=2)

    if watch_lbl.cget('text') == '00:00':
        continue_btn.grid(row=1, columnspan=2, sticky='ew')
    else:
        reset_btn.grid(row=1, columnspan=2, sticky='ew')
        continue_btn.grid(row=2, columnspan=2, sticky='ew')

    root.after_cancel(after_id)



root = Tk()
root.title('Stop Watch')

watch_lbl = Label(root, width=5, font=('Ubuntu', 100), text='00:00')
watch_lbl.grid(row=0, columnspan=2, sticky='ew')

start_btn = Button(root, text='Start', font=('Ubuntu', 30), command=start_sw)
stop_btn = Button(root, text='Stop', font=('Ubuntu', 30), command=stop_sw)
continue_btn = Button(root, text='Continue', font=('Ubuntu', 30), command=continue_sw)
reset_btn = Button(root, text='Reset', font=('Ubuntu', 30), command=reset_sw)
lap_btn = Button(root, text='Lap', font=('Ubuntu', 30), command=lap)
clear_btn = Button(root, text='Clear laps', font=('Ubuntu', 30), command=clear)

start_btn.grid(row=1, columnspan=2, sticky='ew')

root.mainloop()
