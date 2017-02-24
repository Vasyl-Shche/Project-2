import random
import string
import json
from datetime import datetime

length = 16  # кол-во символов в купоне
quantity = 100000  # кол-во купонов
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits  # набор символов для купонов


def mask(c, length): # маски для купонов
    if length == 16:
        c = c[0:4] + '-' + c[4:8] + '-' + c[8:12] + '-' + c[12:16]  # маска на 16 символов
    elif length == 12:
        pass
    elif length == 9:
        pass
    return c


def sugar(length):  # генерим time-stamp заданной длинны
    l = []
    if length == 16:  # для х16
        b = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%S")
        for i in range(0, len(b)):
            l.append(b[i])
    elif length == 12:
        pass
    elif length == 9:
        pass
    return l


def coupon(length):  # ф-я генерации одного купона заданого формата.
    l = []
    for i in range(0, length):
        l.append(random.choice(chars))
    k = sugar(length)
    for i in range(0, length):
        code = int((ord(l[i])+ord(k[i]))/2)
        l[i] = chr(code)
        if l[i] not in chars:
            l[i] = random.choice(string.ascii_lowercase)
    c = ''.join(l)
    c = mask(c, length)
    return c


def generator(quantity):  # THE CORE !!!  генерим купоны в нужном кол-ве
    i = 0
    s = set()
    while i != quantity:
        s.add(coupon(length))
        i = len(s)
    s = list(s)
    return s


def json_writer(s):  # пишем всё это в JSON
    with open('coupon.json', 'w') as f:
        json.dump(s, f)

# print(generator(quantity))
json_writer(generator(quantity))
