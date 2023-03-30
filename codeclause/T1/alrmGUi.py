from tkinter.ttk import*
from tkinter import*

from PIL import ImageTk, Image

bg_color = "white"
co1 = "#566FC6" #blue
co2 = "#ffffff" #white

window = Tk()
window.title(" ")
window.geometry("350x200")
window.configure(bg = bg_color)

frame_line = Frame(window, width= 400, height=5, bg=co1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width= 400, height=290, bg=co2)
frame_body.grid(row=1, column=0)

img = Image.open('clock.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text = "Alarm", height=1, font=('Ivy 20 bold'), bg=bg_color)
name.place(x=127, y=15)

hour = Label(frame_body, text = "Hour", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
hour.place(x=130, y=50)
c_hour = Combobox(frame_body, width=2, font=('arial 13'))
c_hour['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=130,y=70)

min = Label(frame_body, text = "Min", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
min.place(x=180, y=50)
c_min = Combobox(frame_body, width=2, font=('arial 13'))
c_min['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_min.current(0)
c_min.place(x=180,y=70)

sec = Label(frame_body, text = "Sec", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
sec.place(x=230, y=50)
c_sec = Combobox(frame_body, width=2, font=('arial 13'))
c_sec['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0)
c_sec.place(x=230,y=70)

period = Label(frame_body, text = "Period", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
period.place(x=280, y=50)
c_period = Combobox(frame_body, width=3, font=('arial 10'))
c_period['values'] = ("AM", "PM")
c_period.place(x=280,y=70)

selected = IntVar()

radl = Radiobutton(frame_body, font=('aril 10 bold'), value=1, text="Activate", bg=bg_color)
radl.place(x=130,y=100)
    
window.mainloop()
