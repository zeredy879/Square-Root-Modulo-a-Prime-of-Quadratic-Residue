from log import logger


def fermat(a: int, p: int) -> int:
    if p % 4 != 3:
        logger.debug("Fermat Little theorem failed, try other algorithms...")
        return -1
    else:
        logger.info("Fermat Little theorem success!")
        res = pow(a, (p + 1) // 4, p)
        return min(res, p - res)
