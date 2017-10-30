from tkinter import*

class ButPro:         #Добавляю кнопку\эвент для Прокостета
    def __init__(self):
        self.lb = Label()
        self.but = Button(root)
        self.but["text"] = "Prokostet"
        self.but.bind("<Button-1>", self.print)
        self.but.grid(row = 0, column = 1,padx = 20, pady =10)
        self.lb.grid(row = 1, column = 1)
    def print(self,event):
        win = Toplevel(root, bg = "white")
        winlab = Label(win, text="Отправлено прокостету", bg = "red", font=("Helvetica", 16))
        winlab.grid(row=1, column = 2, padx = 100, pady = 70)
        win.minsize(width=400, height=200)
        win.maxsize(width=400, height=200)
        self.lb.configure(text = "yes",bg = 'white', font=(10))

class ButGrich:         #Добавляю кнопку\эвент для Гричина
    def __init__(self):
        self.lbgr = Label()
        self.butgr = Button(root)
        self.butgr["text"] = "Grichin"
        self.butgr.bind("<Button-1>", self.printGr)
        self.butgr.grid(row = 0, column = 3,padx = 20, pady =10)
        self.lbgr.grid(row = 1, column = 3)
    def printGr(self,event):
        wingr = Toplevel(root, bg = "white")
        winlabgr = Label(wingr, text="Отправлено гричину", bg = "red", font=("Helvetica", 16))
        winlabgr.grid(row=1, column = 2, padx = 100, pady = 70)
        wingr.minsize(width=400, height=200)
        wingr.maxsize(width=400, height=200)
        self.lbgr.configure(text = "yes", bg = 'white', font=(10))

root = Tk()  #Создаю главную рамку объекта
root.title('СМСКИ БРАТАНАМ')
root["bg"] = 'white'

def version():
    verswin = Toplevel(root, bg = 'white')
    verslab = Label(verswin,text = "Версия:\n"
                                   "0.1 beta", bg = 'white')
    verswin.maxsize(width=50, height=60)
    verswin.minsize(width=50, height=60)
    verslab.pack()
def kak():
    kakwin = Toplevel(root, bg = 'white')
    kaklb = Label(kakwin, text = 'bla bla bla bla ', bg= 'white')
    kakwin.title('Работа')

    kakwin.maxsize(width=200, height=100)
    kakwin.minsize(width=200, height=100)
    kaklb.pack()

m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label = 'Help', menu= fm)
fm.add_command(label = 'Версия', command = version)
fm.add_command(label = 'Как это все работает', command = kak)

root.minsize(width=400,height=200)
root.maxsize(width=400,height=200)

prokostet = ButPro()
grich = ButGrich()

root.mainloop()
