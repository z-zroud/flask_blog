
class NotExistedException(Exception):
    def __init__(self, *args: object, reason=None):
        super(args)
        self.reason = "object not existed"
        if reason:
            self.reason = reason
        


class HasExistedException(Exception):
    def __init__(self, *args: object, reason=None):
        super(args)
        self.reason = "object has already existed"
        if reason:
            self.reason = reason