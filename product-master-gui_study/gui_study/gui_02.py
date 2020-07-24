# label -> 위젯 한번만 pack, 변동사항은 config로!

import tkinter

window = tkinter.Tk()
label = tkinter.Label(window, text = "hello python", font = ("Courier",14,'bold italic') )
label.pack() # label선언하고 꼭 pack 해주기
label.config(text = "hello")
window.mainloop()

# frame -> 위젯마다 pack

import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
frame2 = tkinter.Frame(window, borderwidth =3, relief=tkinter.SUNKEN)
frame2.pack()

first = tkinter.Label(frame2, text="강가연")
first.pack()
second = tkinter.Label(frame, text="24")
second.pack()
third = tkinter.Label(frame2, text="국사학과") # FRAME이 다를 경우 다른 FRAME을 매개변수로 넣어주기
third.pack()

window.mainloop()

# button
import tkinter
window = tkinter.Tk()
b1 = tkinter.Button(window, width =10, height=10, text = "say hello")
b1.pack()
window.mainloop()

# CheckButton

import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
red = tkinter.IntVar()
green = tkinter.IntVar()
blue = tkinter.IntVar()

# for문을 통해 어떠한 체크박스가 눌렸는지 확인하기
for (name,var) in (('R',red),('G',green),('B',blue)):
    check = tkinter.Checkbutton(frame, text=name,variable = var)
    check.pack(side='left')

def recolor(widget, r, g, b):
    color = '#'
    for var in (r, g, b):
        color +='FF' if var.get() else '00' # RGB 색상표의 색 만들기
    widget.config(bg=color)

label=tkinter.Label(frame, text="[         ]")
button = tkinter.Button(frame, text='update', command=lambda: recolor(label, red, green, blue))
button.pack(side="left")
label.pack(side='left')
window.mainloop()


# entry
import tkinter

window = tkinter.Tk()
var1 = tkinter.StringVar()
label =tkinter.Label(text="안녕? 네 이름은?", font=('Courier',14))
label.pack(side='left')
e1 = tkinter.Entry(window, bd = 5, textvariable = var1)
e1.pack(side='left')
window.mainloop()