def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение. Не верите?', 'alyoha-zachem@gmail.com')
send_email('Вы видите это сообщение, потому что у вас есть глаза', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, оцените это блюдо, я постарался', 'medvedev@mail.ru', sender='chef.gourman@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'l-dar@mail.ru', sender='l-dar@mail.ru')
