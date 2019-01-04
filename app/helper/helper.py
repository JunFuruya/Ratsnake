# -*- coding: UTF-8 -*-

import hashlib
import hmac

class HashHelper():
    @classmethod
    def hexdigest(cls, text):
        # TODO: make config singleton
        secret_key = 'secret_key'
        # TODO: select an appropriate algorithm
        return hmac.new(secret_key.encode('utf-8'), msg=text.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
