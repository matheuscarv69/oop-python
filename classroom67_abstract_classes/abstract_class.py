"""
Classes abstratas - Abstract Base Class (abc)

ABCs são usadas como contratos para a definiçã de novas classes.
Elas podem forçar outras classes a criarem métodos concretos.
Também podem ter métodos concretos por elas mesmas.

@abstractmethods são métodos que não têm corpo.
As regras para classes abstratas com métodos abstratos é que elas
NÃO PODEM ser instânciadas diretamente.

Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).
Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.

É possível criar @property @setter @classmethod, @staticmethod e
@method como abstratos, para isso use @abstractmethod como decorator
mais interno.
"""

from abc import ABC, abstractmethod


# Para uma classe ser abstrata ela precisa herdar de ABC ou de metaclass=ABCMeta
# e possuir pelo menos um método anotado com @abstractmethod
class Log(ABC):

    @abstractmethod
    def _log(self, msg):
        ...

    def log_success(self, msg):
        return self._log(f'Success: {msg}')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')


class LogPrintMixin(Log):

    def _log(self, msg):
        print(f'{msg} - {self.__class__.__name__}')


# Instanciar uma classe abstrata irá gerar o seguinte erro:
# TypeError: Can't instantiate abstract class Log with abstract method _log
# log = Log()

# forma certa: Uma classe precisa herdar a classe abstrata e implementar o
# método abstrato

logPrint = LogPrintMixin()
logPrint.log_success('Hey')
