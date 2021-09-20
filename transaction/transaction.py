from datetime import datetime
from ethereum_tests.deploy.registrar import web3


class Transaction:
    def __init__(self, rec, phrase):
        self.time = datetime.now().timestamp()
        self.rec = rec  # User obj
        self.hashed_phrase = phrase

    def recipient_check(self, input_recipient):
        if self.rec == input_recipient:
            return True
        return False

    def phrase_check(self, phrase):
        if web3.solidityKeccak(phrase) == self.hashed_phrase:
            return True
        return False

    def time_check(self):
        if (datetime.now().timestamp() - self.time) >= 1000000000000:
            return True
        return False

