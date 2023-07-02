from log import logger


def atkin(a: int, p: int) -> int:
    if p % 8 != 5:
        logger.debug("Atkin algorithm failed, try other algorithms...")
        return -1
    else:
        logger.info("Atkin algorithm success!")
        b = pow(2 * a, (p - 5) // 8, p)
        i = (2 * a * (b**2)) % p
        res = (a * b * (i - 1)) % p
        return min(res, p - res)
