from log import logger
import random


def cipolla(a: int, p: int) -> int:
    logger.info("Cipolla algorithm start...")
    b = (p - 1) // 2
    while pow(b**2 - a, (p - 1) // 2, p) == 1:
        b = random.randint(1, p - 1)
    w = (b**2 - a) % p
    logger.info("b found")

    class QuadraticField:
        """if e ∈ Fp2, then e = x + y * i, i = √w"""

        def __init__(self, x, y):
            self.x = x % p
            self.y = y % p

        def __mul__(self, other):
            x = (self.x * other.x + w * self.y * other.y) % p
            y = (self.x * other.y + self.y * other.x) % p
            return self.__class__(x, y)

        def __pow__(self, exp):
            res = self.__class__(1, 0)
            if exp:
                tmp = self.__class__(self.x, self.y)
                while exp:
                    if exp & 1 == 1:
                        res *= tmp
                    tmp *= tmp
                    exp >>= 1
            return res

    res = (pow(QuadraticField(b, 1), (p + 1) // 2).x) % p
    logger.info("Cipolla algorithm finished.")
    return min(res, p - res)
