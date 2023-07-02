from log import logger
import argparse
import sys
from fermat import fermat
from atkin import atkin
from muller import muller
from cipolla import cipolla

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--number", type=int, help="The number", required=True)
parser.add_argument("-p", "--prime", type=int, help="The prime", required=True)
args = parser.parse_args()
a = args.number
p = args.prime


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if isPrime(p) is False:
    logger.debug("The given p is not a prime!!")
    sys.exit(0)

if pow(a, (p - 1) // 2, p) != 1:
    logger.debug("The number a is not a Quadratic Residue!!")
    sys.exit(0)

algorithms = [fermat, atkin, muller, cipolla]
for alg in algorithms:
    res = alg(a, p)
    if res != -1:
        logger.info("The square root found!!")
        logger.info(str(res) + " ^ 2 = " + str(a) + " mod " + str(p))
        logger.info(str(p - res) + " ^ 2 = " + str(a) + " mod " + str(p))
        sys.exit(0)
