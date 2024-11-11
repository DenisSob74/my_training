
def send_email(message: str, recipient: str, sender="university.help@gmail.com"):

    ending = ('.com', '.ru', '.net')
    if "@" not in recipient or "@" not in sender or not recipient.endswith(ending)\
            or not sender.endswith(ending):
        print(f"Невозможно отправить письмо с адреса < {sender} > на адрес < {recipient} > .")

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    elif sender != 'university.help@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса < {sender} > на адрес < {recipient} > .")

    else:
        print(f"Письмо успешно отправлено с адреса < {sender} > на адрес < {recipient} > .")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')