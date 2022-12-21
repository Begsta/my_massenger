from tkinter.messagebox import *

Useres = dict()




#функция для того чтобы предупредить пользователя что он(а) вошёл
def printf(bool_):
    if bool_ == True:
        showinfo("У вас хороший пароль!", "Вы зарегистрированы")

#для проверки пароля
def normal_password(password):
    if len(password) < 8:
        showerror("Ошибка!", "пароль слишком короткий")
        return False
    array_symbol = [str(i) for i in range(0, 10)]
    array1 = ['_', '-', '/', '.', ',']
    temp = [False , False , False]
    for i in range(0, len(password)):
        if password[i] == password[i].upper():
            temp[0] = True
        if password[i] in array_symbol:
            temp[1] = True
        if password[i] in array1:
            temp[2] = True
        if ((temp[0] == True) and (temp[0] == temp[1] == temp[2])):
            return True
    showerror("Ошибка!", f"Не надёжный пароль!\n{temp[0]}, {temp[1]}, {temp[2]}")
    return False

#приложение для хэширования пароля(В процессе)
def hash(password):
    hash_password= ""
    for i in password:
        hash_password += ord(i)
    hash_password = int(hash_password, 16)
    return hash_password

# если забыл пароль, то это функция заменит его
def forget_password(login, password):
    if login not in Useres.keys():
        showerror("Ошибка!", "У вас нет аккаунта.")
        return
    elif password == Useres[login][0]:
        showinfo('', f"Это ваш пароль {password}")
    elif normal_password(password):
        Useres[login][0] = password

#функция для регистрации пользования
def registration(login, password):
    if login in Useres.keys():
        showerror("Ошибка", "У вас уже есть аккаунт")
        return
    elif normal_password(password):
        Useres[login] = [password]
        return printf(True)
