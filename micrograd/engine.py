class Value:

    def __init__(self, data, _children=(), _op=""):
        self.data = data
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        return Value(self.data + other.data, _children=(self, other), _op="+")

    def __mul__(self, other):
        return Value(self.data * other.data, _children=(self, other), _op="*")