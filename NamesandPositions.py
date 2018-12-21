from tkinter import *

#1 - Functions
def enter():
    text_input = entry.get()
    output.delete(0.0, END)
    if text_input in myDict:
        info = myDict[text_input]
    else:
        info = 'Info not found.'
    output.insert(END, info)

#2 - Structure
Window = Tk()
Window.title('Demonstration')
Window.geometry('400x300')
Window.configure(background='black')
Lb = Label(Window, text='Insert Here', bg='black', fg='white', font=('Kalimati', '12'))
Lb.grid(row=0, column=0)
entry = Entry(Window, width=20, bg='white')
entry.grid(row=2, column=0, sticky=W)
Button(Window, text='Submit', width=6, command=enter).grid(row=3, column=0, sticky=W)
Label(Window, text='\nInformation:', bg='black', fg='white', font=('Kalimati', '12')).grid(row=4, column=0, sticky=W)
output = Text(Window, width=80, height=8, wrap=WORD, background='white')
output.grid(row=8, column=0, columnspan=2, sticky=W)

#3 - Dictionary
myDict = {'Dorgival':'Commander', 'Johnson':'Captain', 'Ayumi':'Captain', 'Cecilia':'Commander'}

#4 - Exit Function
def close_Window():
    Window.destroy()
    exit()

#5 - Exit
Label(Window, text='Click Here to Exit', bg='black', fg='white', font=('Kalimati', '12')).grid
Button(Window, text='Exit', width=4, command=close_Window).grid(row=7, column=0, sticky=W)

#6 - Exit Function
Window.mainloop()