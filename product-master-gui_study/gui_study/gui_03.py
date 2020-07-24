import tkinter as tk

w = tk.Tk()

# 모델
counter = tk.IntVar()
counter.set(0)

# 컨트롤러
def click(var, value):
    var.set(var.get()+value)

# 뷰
frame = tk.Frame(w)
frame.pack()
button = tk.Button(frame, text='Up', command = lambda:click(counter,1))
button.pack()

button = tk.Button(frame,text='Down',command=lambda:click(counter,-1))
button.pack()

label = tk.Label(frame,textvariable=counter)
label.pack()

w.mainloop()