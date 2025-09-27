class Token:
    def __init__(self, type: str, value: str, priority: int):
        self.type = type
        self.value = value
        self.priority = priority

    type: str  # тип токена NUMBER, OP...
    value: str
    priority: int
