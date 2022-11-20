from log import LogFileMixin, LogPrintMixin

log_print = LogPrintMixin()
log_print.log_error('whatever')
log_print.log_success("It's works")

log_file = LogFileMixin()
log_file.log_error('whatever')
log_file.log_success("It's works")
