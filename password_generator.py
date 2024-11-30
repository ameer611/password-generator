import string
import random


def generate_password(length_of_password):
    str_upper = string.ascii_uppercase
    str_lower = string.ascii_lowercase
    numbers = string.digits
    punctuations = string.punctuation

    list_ = []
    list_.extend(list(str_upper))
    list_.extend(list(str_lower))
    list_.extend(list(numbers))
    list_.extend(list(punctuations))

    random.shuffle(list_)
    password = ''.join(list_[:int(length_of_password)])
    return password

length = input('Enter the password length: -> ' )
print(generate_password(length))
