from tkinter import *
from tkinter.ttk import *
from Data_base import *

# root window
root = Tk()
root.geometry('800x600')
root.title('Messenger')
root["bg"] = "Black"

#создание текстов
lb1 = Label(root, text="Введите логин: ", width= "19")
lb2 = Label(root, text= "Введите пароль:", width= "19")

#создание вводных строк
ent_login = Entry(root, width="25", )
ent_password = Entry(root, show='*', width= "25")

#создание кнопок
bt_SING_IN = Button(root, text="Вход", width= "18", command=lambda: sing_in(login=ent_login.get(), password=ent_password.get()))
bt_RING_IN = Button(root, text= "Зарегистрироваться", width= "18", command=lambda: registration(ent_login.get(), ent_password.get()))
bt_show_password = Button(root, text= "Показать пароль", width="18", command=lambda: showinfo("Показать пароль", ent_password.get()))
#замещение
lb1.grid(row=0, column=0)
lb2.grid(row= 2, column=0)
ent_login.grid(row=0, column=1)
ent_password.grid(row=2, column=1)
bt_SING_IN.grid(row=3, column=0)
bt_RING_IN.grid(row=4, column=0)
bt_show_password.grid(row=2, column=3)
#зацикливание окна
root.mainloop()
