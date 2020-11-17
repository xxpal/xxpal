class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i
        return

    def __repr__(self) -> str:
        return str(self.val)

    # The first argument to every method is always "self",
    # and its value is supplied by the Python interpreter.
    def increase(self) -> None:
        self.val += self.incr
        return
