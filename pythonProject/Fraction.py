class MyError(Exception):
    def __init__(self, text):
        self.text = text


class Fraction:

    def __init__(self, numerator: int, denominator: int):
        # assert isinstance(denominator, int) and denominator != 0 \
        #        and isinstance(numerator, int)
        if not isinstance(denominator, int) or not isinstance(numerator, int):
            raise MyError("denominator or numerator    is no int")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        if self.denominator != 0:
            if isinstance(other, int):
                return Fraction(
                    numerator=self.numerator + self.denominator * other,
                    denominator=self.denominator
                )

            elif isinstance(other, Fraction):
                return Fraction(
                    numerator=self.numerator * other.denominator + self.denominator * other.numerator,
                    denominator=self.denominator * other.denominator
                )
            else:
                return None

        else:
            return None

    def __sub__(self, other):
        if self.denominator != 0:
            if isinstance(other, int):
                return Fraction(
                    numerator=self.numerator - self.denominator * other,
                    denominator=self.denominator
                )
            elif isinstance(other, Fraction):
                return Fraction(
                    numerator=self.numerator * other.denominator - self.denominator * other.numerator,
                    denominator=self.denominator * other.denominator
                )
            else:
                return None
        else:
            return None

    def __mul__(self, other):
        if self.denominator != 0:
            if isinstance(other, int):
                return Fraction(
                    numerator=self.numerator * other,
                    denominator=self.denominator
                )

            elif isinstance(other, Fraction):
                return Fraction(
                    numerator=self.numerator * other.numerator,
                    denominator=self.denominator * other.denominator
                )

            else:
                return None
        else:
            return None

    def __truediv__(self, other):
        if self.denominator != 0:
            if isinstance(other, int):
                return Fraction(
                    numerator=self.numerator * other.denominator,
                    denominator=self.denominator * other.numerator
                )
            elif isinstance(other, Fraction):
                return Fraction(
                    numerator=self.numerator * other.denominator,
                    denominator=self.denominator * other.numerator
                )

            else:
                return None

        else:
            return None

    def __pow__(self, power):
        if isinstance(power, int):
            return Fraction(
                numerator=self.numerator ** power,
                denominator=self.denominator ** power
            )
        elif isinstance(power, float):
            tmp = self.numerator ** power \
                  / self.denominator ** power
            self.from_float_to_frac(tmp)
            return self.copy()

    def __radd__(self, other):
        if self.denominator != 0:
            if isinstance(other, int):
                return Fraction(
                    numerator=self.numerator + self.denominator * other,
                    denominator=self.denominator
                )

            elif isinstance(other, Fraction):
                return Fraction(
                    numerator=self.numerator * other.denominator + self.denominator * other.numerator,
                    denominator=self.denominator * other.denominator
                )
            else:
                return None
        else:
            return None

    def __rsub__(self, other):
        if self.denominator != 0:
            if isinstance(other, int):
                return Fraction(
                    numerator=self.numerator - self.denominator * other,
                    denominator=self.denominator
                )
            elif isinstance(other, Fraction):
                return Fraction(
                    numerator=self.numerator * other.denominator - self.denominator * other.numerator,
                    denominator=self.denominator * other.denominator
                )
            else:
                return None

    def __rmul__(self, other):
        if self.denominator != 0:
            if isinstance(other, int):
                return Fraction(
                    numerator=self.numerator * other,
                    denominator=self.denominator
                )

            elif isinstance(other, Fraction):
                return Fraction(
                    numerator=self.numerator * other.numerator,
                    denominator=self.denominator * other.denominator
                )


            else:
                return None
        else:
            return None

    def __rtruediv__(self, other):
        if self.denominator != 0:

            if isinstance(other, int):
                return Fraction(
                    numerator=self.numerator * other.denominator,
                    denominator=self.denominator * other.numerator
                )
            elif isinstance(other, Fraction):
                return Fraction(
                    numerator=self.numerator * other.denominator,
                    denominator=self.denominator * other.numerator
                )

            else:
                return None

    def reduction(self):
        if self.denominator != 0:
            if self.denominator > self.numerator:
                for i in range(-1000, 1001):
                    if self.numerator < 0 and self.denominator < 0 and i != 1 and self.denominator % i == 0 and self.numerator % i == 0:
                        return Fraction(numerator=int(self.numerator * i ** (-1)),
                                        denominator=int(self.denominator * i ** (-1)))

                    elif i != 1 and self.denominator % i == 0 and self.numerator % i == 0:
                        return Fraction(numerator=int(self.numerator * i ** (-1) * (-1)),
                                        denominator=int(self.denominator * i ** (-1)) * (-1))
            elif self.numerator > self.denominator:
                for i in range(-1000, 1001):
                    if self.numerator < 0 and self.denominator < 0 and i != 1 and self.denominator % i == 0 and self.numerator % i == 0:
                        return Fraction(numerator=int(self.numerator * i ** (-1)),
                                        denominator=int(self.denominator * i ** (-1)))
                    elif i != 1 and self.denominator % i == 0 and self.numerator % i == 0:
                        return Fraction(numerator=int(self.numerator * i ** (-1) * (-1)),
                                        denominator=int(self.denominator * i ** (-1) * (-1)))

            if self.denominator % self.numerator == 0:
                return Fraction(numerator=int(self.numerator * self.numerator ** (-1)),
                                denominator=int(self.denominator * self.numerator ** (-1)))
            elif self.numerator % self.denominator == 0:
                return Fraction(numerator=int(self.numerator * self.denominator ** (-1)),
                                denominator=int(self.denominator * self.denominator ** (-1)))
            else:
                return Fraction(numerator=self.numerator, denominator=self.denominator)
        else:
            return None

    def celaya_cast(self):
        if self.denominator != 0:
            whole_part = self.numerator // self.denominator
            fract_part = self.numerator % self.denominator
            return ("{} + {}/{}".format(whole_part, fract_part, self.denominator))

    def from_float_to_frac(self, in_float: float):
        tmp = str(in_float)
        tmp_list = tmp.split('.')
        whole_part = int(tmp_list[0])
        tens_pow = 10 ** len(tmp_list[1])
        whole_part = tens_pow * whole_part + int(tmp_list[1])
        self.numerator = whole_part
        self.denominator = tens_pow

    def __int__(self):
        return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator

    def copy(self):
        return Fraction(
            numerator=self.numerator,
            denominator=self.denominator
        )
