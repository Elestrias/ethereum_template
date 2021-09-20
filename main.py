import sys
from threading import Thread

# from app import app
# from desktop import QApplication, Application

from transaction import transaction_list, transaction_time_loop

if __name__ == '__main__':
    """
    server_thread = Thread(target=app.run, daemon=True, kwargs={'port': 5000,
                                                                'threaded': True,
                                                                'debug': True,
                                                                'use_reloader': False}).start()
                                                                """
    transaction_time_check = Thread(target=transaction_time_loop()).start()

    # desktop_app = QApplication(sys.argv)
    # ex = Application()
    # ex.show()
    # sys.exit(desktop_app.exec_())
