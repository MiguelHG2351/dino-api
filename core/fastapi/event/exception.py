class InvalidEventTypeException(Exception):
    def __init__(self):
        super().__init__('Event must be inherit event')

class InvalidParameterTypeException(Exception):
    def __init__(self):
        super().__init__('Parameter must inherit BaseModel')

class EmptyContextException(Exception):
    def __init__(self):
        super().__init__('Event context is empty. check if middleware configured well')

class ParameterCountException(Exception):
    def __init__(self):
        super().__init__('Event has to many parameters')

class RequiredParameterException(Exception):
    def __init__(self):
        super().__init__('Event context is empty. check if middleware configured well')
