"""
Abstraction

log class like an interface at this moment.
"""

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:

    # method contract
    def _log(self, msg):
        raise NotImplementedError('Implement the log method')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')


class LogFileMixin(Log):

    def _log(self, msg):
        formatted_msg = f'{msg} - {self.__class__.__name__}'

        print(f'Saving in log: {formatted_msg}')

        with open(LOG_FILE, 'a') as file:
            file.write(formatted_msg)
            file.write('\n')


class LogPrintMixin(Log):

    def _log(self, msg):
        print(f'{msg} - {self.__class__.__name__}')


if __name__ == '__main__':
    log_print = LogPrintMixin()
    log_print.log_error('whatever')
    log_print.log_success("It's works")

    log_file = LogFileMixin()
    log_file.log_error('whatever')
    log_file.log_success("It's works")
