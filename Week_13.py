import random

def get_n_random_integer(n):
    random.seed(10) # ayni random degerlere ulasmak icin 
    numbers = []
    for i in range(n):
        s = random.randint(-10,10)
        numbers.append(s)
    return numbers


def get_mean_for_n_integer(numbers):
    toplam = 0
    kactane = 0
    for sayi in numbers:
        toplam += sayi
        kactane += 1
    return toplam/kactane


def get_std_for_n_integer(numbers):
    toplam = 0
    kactane = 0
    ortalama = get_mean_for_n_integer(numbers)
    
    for sayi in numbers:
        toplam = toplam +(sayi-ortalama)**2
        kactane += 1
    var_1 = toplam/(kactane-1)
    std_1 = var_1**0.5
    return std_1


def normalizasyon(numbers):
    new_numbers = []
    ortalama = get_mean_for_n_integer(numbers)
    standart_sapma = get_std_for_n_integer(numbers)
    for x in numbers:
        new_x = (x-ortalama)/standart_sapma
        new_numbers.append(new_x)
    return new_numbers
