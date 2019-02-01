import os
import sys
import timeit

max_num_to_consider = int(sys.argv[1])


# for python version
import python.sieve

print("running regular python version")
start = timeit.default_timer()
primes = python.sieve.get_primes(max_num_to_consider)
print("found {} primes".format(len(primes)))
stop = timeit.default_timer()
print("Regular python version took: {:.2f}s\n".format(stop - start))


# for c version
# gcc sieve.c -O3 -o sieve

print("running regular c version")
start = timeit.default_timer()
os.system('./c/sieve {}'.format(max_num_to_consider))
stop = timeit.default_timer()
print("Regular c version took: {:.2f}s\n".format(stop - start))


# for cython version
# python3 setup_cython_sieve.py build_ext --inplace
import cython_imp.sieve 

print("running cython version")
start = timeit.default_timer()
primes = cython_imp.sieve.get_primes(max_num_to_consider)
print("found {} primes".format(len(primes)))
stop = timeit.default_timer()
print("cython version took: {:.2f}s\n".format(stop - start))


# for cython c wrapper version
# python3 setup_cython_wrap_c_sieve.py build_ext --inplace
import wrap_c_cython.sieve 

print("running cython c wrapper version")
start = timeit.default_timer()
primes = wrap_c_cython.sieve.get_primes(max_num_to_consider)
print("found {} primes".format(len(primes)))
stop = timeit.default_timer()
print("cython c wrapper version took: {:.2f}s\n".format(stop - start))


# for ctypes version
# gcc sieve.c -O3 -fPIC -shared -o libsieve.so 
import wrap_c_ctypes.sieve

print("running ctypes version")
start = timeit.default_timer()
primes = wrap_c_ctypes.sieve.get_primes(max_num_to_consider)
print("found {} primes".format(len(primes)))
stop = timeit.default_timer()
print("ctypes version took: {:.2f}s\n".format(stop - start))


# for python/c api version
# sudo python3 setup_python_c_api_sieve.py install
import wrap_c_api_sieve

print("running python/c api version")
start = timeit.default_timer()
primes = wrap_c_api_sieve.get_primes(max_num_to_consider)
print("found {} primes".format(len(primes)))
stop = timeit.default_timer()
print("python/c api version took: {:.2f}s\n".format(stop - start))
