"""
Polimorfismo em Python Orientado a Objetos

Polimorfismo é o princípio que permite que classes derivadas de
uma mesma superclasse tenham métodos iguais (com mesma assinatura)
mas comportamentos diferentes.

Assinatura do método = Mesmo nome e quantidade de parâmetros
(retorno não faz parte da assinatura)

Opinião + princípios que contam:

Assinatura do método: nome, parâmetros e retorno iguais
 SO"L"ID

 Princípio da substituição de liskov

 Objetos de uma superclasse devem ser substituíveis por objetos de
 uma subclasse sem quebrar a aplicação.

Sobrecarga de métodos (overload)  🐍 = ❌
Sobreposição de métodos (override) 🐍 = ✅
"""

from abc import ABC, abstractmethod


class Notification(ABC):

    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def send(self) -> bool:
        ...


class NotificationSMS(Notification):

    def send(self) -> bool:
        print(f'Sending SMS: {self.msg}')
        return True


class NotificationEmail(Notification):

    def send(self) -> bool:
        print(f'Sending email: {self.msg}')
        return False


# Polymorphism
def to_notify(notification: Notification):
    print(f'LOG - TO NOTIFY METHOD - {notification.__class__.__name__}')
    notification_sent = notification.send()
    print()

    if not notification_sent:
        raise Exception(f'Notification: {notification.__class__.__name__} not sent')


sms_notification = NotificationSMS('SMS Notification Test')
email_notification = NotificationEmail('EMAIL Notification Test')

to_notify(sms_notification)
to_notify(email_notification)
