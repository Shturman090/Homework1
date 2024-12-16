def send_email(message, recipient, sender = "university.help@gmail.com"):
    if ('@' not in recipient and '@' not in sender or not (
            recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'))) or \
            ('@' not in sender or not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")


    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")




send_email('messagie', 'vasyok1337@gmail.com')
send_email('messagie', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('messagie', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('messagie', 'university.help@gmail.com')
