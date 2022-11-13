from pprint import pprint
dict_bin = [{'bin': bin(i), 'dec': i, 'oct': oct(i), 'hex': hex(i)} for i in range(16)] #перебирая числа от 0 до 15, создаю список словарей, каждый из которых включает в себя требуемые пары ключ-значение
pprint(dict_bin) #помогает представить информацию в красивом виде
