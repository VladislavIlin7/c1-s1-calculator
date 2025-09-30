class Token:
    def __init__(self, type_t: str, value: str, priority: int):
        self.type_token = type_t
        self.value = value
        self.priority = priority

    type_token: str
    value: str
    priority: int