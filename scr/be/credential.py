# Standard Modules
import os
import base64

class bncCred:
    def __init__(self):
        self.__user = os.getenv('BNCUSER')
        self.__apiKey = os.getenv('BNCAPIKEY')
        self.__secret = os.getenv('BNCSECRET')
        
    @property
    def user(self):
        return base64.b64decode(self.__user.encode("ascii")).decode("ascii")
        
    @property
    def apiKey(self):
        return base64.b64decode(self.__apiKey.encode("ascii")).decode("ascii")
        
    @property
    def secret(self):
        return base64.b64decode(self.__secret.encode("ascii")).decode("ascii")
    
