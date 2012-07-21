import string

CLASS_ID_SEED = 10235

class BaseConverter(object):
    decimal_digits = "0123456789"

    def __init__(self, digits, seed=0):
        self.seed = seed
        self.digits = digits

    def from_num(self, i):
        i = i + self.seed
        return self.convert(i, self.decimal_digits, self.digits)

    def to_num(self, s):
        return int(self.convert(s, self.digits, self.decimal_digits)) - self.seed

    def convert(number, fromdigits, todigits):
        # Based on http://code.activestate.com/recipes/111286/
        if str(number)[0] == '-':
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
           x = x * len(fromdigits) + fromdigits.index(digit)

        # create the result in base 'len(todigits)'
        if x == 0:
            res = todigits[0]
        else:
            res = ""
            while x > 0:
                digit = x % len(todigits)
                res = todigits[digit] + res
                x = int(x / len(todigits))
            if neg:
                res = '-' + res

        return res

    convert = staticmethod(convert)

class_id_converter = BaseConverter(string.digits + string.ascii_uppercase, CLASS_ID_SEED)
