from . import transaction_list


def transaction_time_loop():
    while True:
        for transaction in transaction_list:
            if not transaction.time_check():
                del transaction
                continue
