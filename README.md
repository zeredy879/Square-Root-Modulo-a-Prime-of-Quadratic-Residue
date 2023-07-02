## Overview

Collections of algorithms to find square root of a number modulo a prime.

Already have implemented some special cases when the prime has good properties such as 
Atkin algorithm when the prime `p` satisfies the condition that `p % 8 == 5`.

## Usage

```shell
$ python3 main.py
usage: main.py [-h] -a NUMBER -p PRIME
```
The square root will output if it exists.

## Done
- [x] Cipolla Algorithm
- [x] Fermat Little Theorem (`p % 4 = 3`)
- [x] Atkin Algorithm (`p % 8 = 5`)
- [x] Muller Algorithm (`p % 16 = 9`)

## TODO

- [ ] Tonelli-Shanks Algorithm
- [ ] Legendre Algorithm
- [ ] Bostan–Mori Algorithm
- [ ] Rotaru Algorithm

## Reference 
1. https://oi-wiki.org/math/number-theory/quad-residue/

2. Shanks, D.: Five number-theoretic algorithms, Proceedings of the second Manitoba conference on numerical mathematics (R. Thomas, H. Williams, Eds.), 7, Utilitas Mathematica, 1973.

3. Müller, S.: On the Computation of Square Roots in Finite Fields, Designs, Codes and Cryptography, 31(3), 2004.

4. Armand Stefan Rotaru: A Complete Generalization of Atkin’s Square Root Algorithm, 2013.
   
5. Alin Bostan and Ryuhei Mori: A Simple and Fast Algorithm for Computing the N-th Term of a Linearly Recurrent Sequence, 2021.