from tkinter import *
from tkinter.ttk import *
from Data_base import *

# создание окна
root = Tk()
root.geometry('800x600')
root.title('Messenger')
root["bg"] = "Black"
Notebook1 = Notebook()

# создание фрейма
login_frame = Frame(root) # фрейм для регистрации и чтобы зайти в аккаунт
Main_frame = Frame(root) # фрейм с письмами


#создание текстов
lb1 = Label(login_frame, text="Введите логин: ", width= "19")
lb2 = Label(login_frame, text= "Введите пароль:", width= "19")

#создание вводных строк
ent_login = Entry(login_frame, width="25", )
ent_password = Entry(login_frame, show='*', width= "25")

#создание кнопок
bt_SING_IN = Button(login_frame, text="Вход", width= "18", command=lambda: sing_in(login=ent_login.get(), password=ent_password.get()))
bt_RING_IN = Button(login_frame, text= "Зарегистрироваться", width= "18", command=lambda: registration(ent_login.get(), ent_password.get()))
bt_show_password = Button(login_frame, text= "👁", width="2", command=lambda: showinfo("Ваш пароль:", ent_password.get()))
bt_Forget_pasword = Button(login_frame, text="Сменить пароль", width="18",command=lambda: forget_password(ent_login.get(), ent_password.get()))

#замещение
login_frame.pack()
lb1.grid(row=0, column=0)
lb2.grid(row= 2, column=0)
ent_login.grid(row=0, column=1)
ent_password.grid(row=2, column=1)
bt_SING_IN.grid(row=3, column=1)
bt_Forget_pasword.grid(row=4, column=1)
bt_RING_IN.grid(row=5, column=1)
bt_show_password.grid(row=2, column=3)

#зацикливание окна
root.mainloop()
