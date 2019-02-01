# sieve_demo
Demo of implementing Sieve of Eratosthenes in python, c, and hybrid approaches

The Sieve of Eratosthenes is a method of generating prime numbers. See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

This project includes the following implementations:
- python only
- c only
- cython called from python
- c wrapped with cython called from python
- c wrapped with python using ctypes
- c wrapped with python using the python/c api

The script run_get_primes.py contains instructions for running the various implementations. 

Sample output for generating all primes up to 100,000:
```
$python3 run_get_primes.py 100000
found 9592 primes
running regular python version
found 9592 primes
Regular python version took: 15.67s

running regular c version
Regular c version took: 1.14s

running cython version
found 9592 primes
cython version took: 9.22s

running cython c wrapper version
found 9592 primes
cython c wrapper version took: 1.12s

running ctypes version
found 9592 primes
ctypes version took: 1.18s

running python/c api version
found 9592 primes
python/c api version took: 1.12s
```
