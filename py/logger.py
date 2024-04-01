import psutil
import logging

def log(date):
    logging.basicConfig(level=logging.INFO, filename="logger.log", filemode="w")

    log_message = ""

    log_header = f"[{date}] Exceeding the critical value \n"
    log_message += log_header

    for pid in psutil.pids():
        log = f"\tPID: {psutil.Process(pid).pid} - {psutil.Process(pid).name()}\n"
        log_message += log

    logging.info(log_message)

# log()