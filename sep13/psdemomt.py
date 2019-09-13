"""demo for the threading"""

import threading
import multiprocessing
import logging
from time import sleep

logging.basicConfig(format='%(threadName)s : %(message)s', level=logging.DEBUG)


def worker(thread_lock):
    """thread function"""
    t_id = threading.current_thread().ident  # thread_id
    t_name = threading.current_thread().name
    sleep(1)
    logging.debug('check for the lock')

    with thread_lock:
        logging.debug('acquired the lock')
        sleep(1)
        logging.debug(f"OUTPUT>>{t_name} : {t_id} <<OUTPUT")
        logging.debug('releases the lock')


def main():
    """main thread"""
    lock = threading.Lock()

    for item in range(1, 6):
        t = threading.Thread(target=worker, args=(lock,))
        t.start()

    parent = threading.current_thread()
    print(parent.name, 'prepares to terminates')


if __name__ == '__main__':
    main()
