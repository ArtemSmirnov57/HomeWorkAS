# Lesson 8 dz 1 Smirnov Artem

from re import compile


def email_parse(email):
    re_mail = compile(r'([\w]+)\@((?<=@)[^.]+\.\w+)')
    if re_mail.match(email):
        n, d = re_mail.findall(email)[0]
        print(dict(username=n, domain=d))
    else:
        raise ValueError


try:
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrains.ru')
except ValueError:
    print(f'Wrong email')
