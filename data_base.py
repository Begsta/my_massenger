from tkinter.messagebox import *
Useres = {
    "begsta": ["qwerty"]
}

def get_ent(ent):
    return ent.get(),

def sing_in(login,password):
    if login not in Useres.keys():
        showinfo("Ошибка", "Вы не зарегистрировались")
    elif Useres[login] == password:
        showinfo("Вход!", "Вы вошли")
    else:
        showinfo("Ошибка", "Пароль не верный!")


def hash(password):
    hash_password=""
    for i in password:
        hash_password += ord(i)
    return hash_password
