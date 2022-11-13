import random
import string
from random import sample

def get_random_password(n=8):
    alphabet = string.ascii_uppercase + string.ascii_lowercase +string.digits #алфавит для пароля
    password_list = random.sample(alphabet, n) #список случайных символов из алфавита
    password = "" #пустой пароль
    for i in range(n):
        password += str(password_list[i]) #привожу список к строке
    return password

print(get_random_password())
