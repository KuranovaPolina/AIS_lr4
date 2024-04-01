import smtplib
import email

from passwords import stmc

def send_email(from_addr, to_addr, subject, text, encode='utf-8'):
    # оставшиеся настройки
    passwd = stmc

    # 123qwerty678!
    server = "smtp.yandex.ru"
    port = 587
    charset = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    # формируем тело письма
    body = "\r\n".join((f"From: {from_addr}", f"To: {to_addr}", 
           f"Subject: {subject}", mime, charset, "", text))

    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(from_addr, passwd)
        # пробуем послать письмо
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()

def send_mail_main():
    from_addr = "kuranovapolina16@yandex.ru"
    to_addr = "kuranovapolina16@yandex.ru"
    subject = "Сервер Python"
    text = "На сервере произошел переход через Критические параметры"
    send_email(from_addr, to_addr, subject, text)

if __name__ == "__main__":
    from_addr = "kuranovapolina16@yandex.ru"
    to_addr = "kuranovapolina16@yandex.ru"
    subject = "Тестовое письмо от Python."
    text = "Отправкой почты управляет Python!"
    send_email(from_addr, to_addr, subject, text)
