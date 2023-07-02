from log import logger
import random


def muller(a: int, p: int) -> int:
    if p % 16 != 9:
        logger.debug("Muller algorithm failed, try other algorithms...")
        return -1
    else:
        logger.info("Muller algorithm success!")
        alpha = pow(2 * a, (p - 9) // 16, p)
        beta = (2 * a * alpha * alpha) % p
        if pow(2 * a, (p - 1) // 4, p) == p - 1:
            res = (alpha * a * (beta - 1)) % p
        else:
            d = (p - 1) // 2
            while pow(d, (p - 1) // 2, p) == 1:
                d = random.randint(1, p - 1)
            alpha = pow(2 * a * d * d, (p - 9) // 16, p)
            beta = pow(2 * a * d * d, (p - 1) // 8, p)
            res = (alpha * a * d * (beta - 1)) % p
        return min(res, p - res)
