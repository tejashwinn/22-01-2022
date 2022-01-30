import hashlib


class Password_Hasher():

    def __init__(self, plain_text, hashed_password=None):

        self.plain_text = plain_text

        if hashed_password is not None:
            self.hashed_password = hashed_password
            self.correct_password = False
            self.check_hashed_password()
        else:
            self.generate_hash()

    def generate_hash(self):
        plaintext = str(self.plain_text).encode()
        d = hashlib.sha256(plaintext)
        self.hashed_password = d.hexdigest()

    def check_hashed_password(self):
        plaintext = str(self.plain_text).encode()
        d = hashlib.sha256(plaintext)
        d1 = d.hexdigest()
        d2 = self.hashed_password
        self.correct_password = d1 == d2
