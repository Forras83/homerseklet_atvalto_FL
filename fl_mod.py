from decimal import Decimal, InvalidOperation

class FLConverter:
    def __init__(self):
        self.units = ("C","F","K")
    def into(self, v, src, dst):
        return fl_convert(v, src, dst)

def fl_parse_input(s: str):
    try:
        return Decimal(str(s).strip())
    except InvalidOperation:
        return None

def fl_format_output(v):
    if v is None:
        return ""
    q = v.quantize(Decimal("0.01"))
    return f"{q.normalize()}"
from decimal import Decimal, InvalidOperation

def fl_parse_input(s: str):
    try:
        return Decimal(str(s).strip().replace(",", "."))
    except InvalidOperation:
        return None


def fl_convert(v, src, dst):
    if v is None:
        return None
    if src == dst:
        return v
    if src == "C" and dst == "F":
        return v*Decimal("9")/Decimal("5")+Decimal("32")
    if src == "F" and dst == "C":
        return (v-Decimal("32"))*Decimal("5")/Decimal("9")
    if src == "C" and dst == "K":
        return v+Decimal("273.15")
    if src == "K" and dst == "C":
        return v-Decimal("273.15")
    if src == "F" and dst == "K":
        return (v-Decimal("32"))*Decimal("5")/Decimal("9")+Decimal("273.15")
    if src == "K" and dst == "F":
        return (v-Decimal("273.15"))*Decimal("9")/Decimal("5")+Decimal("32")
    return None