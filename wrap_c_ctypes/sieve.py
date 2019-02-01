import ctypes

_sieve = ctypes.CDLL('./wrap_c_ctypes/libsieve.so')

class PrimesStruct(ctypes.Structure):
    _fields_ = [('num_primes', ctypes.c_int), ('primes', ctypes.POINTER(ctypes.c_int))]

def get_primes(max_num_to_consider):
    _sieve.get_primes.argtypes = (ctypes.c_int,)
    _sieve.get_primes.restype = ctypes.POINTER(PrimesStruct)

    result = _sieve.get_primes(ctypes.c_int(max_num_to_consider))

    primes = []
    for i in range(0, result.contents.num_primes):
        primes.append(result.contents.primes[i])

    # Need to call back to c to free memory
    _sieve.free_primes_struct(result)
    
    return primes

