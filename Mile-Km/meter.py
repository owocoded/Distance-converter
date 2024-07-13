# when u are working with tkinter:
# widget(button, text or entery field)
# layout(This determine how the widget are arrange on the windows)
# style(the determine the style of the GUI)



import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk

def convert():
    # 1 way to get acess to the entry oage
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)
# window
window = tk.Tk()

#setting a title
window.title("demo")

#setting the width and height
window.geometry('300x150')

#title, note: the label shuould be inside a parent which is window
title_label = ttk.Label(master= window, text= "Miles to kilometers", font='Calibri 24 bold' )


#how to make the ttk values show on the window
title_label.pack()

#how to create a frame
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='convert', command=convert)

entry.pack(side= 'left', padx= '10')
button.pack(side = 'left')
input_frame.pack()

# #creating another frame
# input_name = ttk.Frame(master=window)
# input = ttk.Entry(master=input_frame)
# button = ttk.Button(master=input_frame, text= 'submit')
#
# input.pack(side='left', padx= '10')
# button.pack(side= 'left')
# input_name.pack(pady= '10')

output_string = tk.StringVar()
output_label = ttk.Label(master= window, text= "output", font='Calibri 24', textvariable=output_string )
output_label.pack()

#to call it to display in window
window.mainloop()