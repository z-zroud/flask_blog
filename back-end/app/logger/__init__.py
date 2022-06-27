import logging
import os
import logging.config
import json

class Log:
    __obj = False
    def __new__(cls, *args, **kwargs):
        if not cls.__obj:
            cls.__obj = super().__new__(cls,*args,**kwargs)
        return cls.__obj

    def __init__(self):
        log_path = os.path.join('conf', os.path.dirname(os.path.abspath(__file__)),"LogConfig.json")
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                logging.config.dictConfig(json.load(f))
        else:
            logging.basicConfig(filename='blog.log', level=logging.INFO)
        self.logger = logging.getLogger('ssss')




log = Log().logger