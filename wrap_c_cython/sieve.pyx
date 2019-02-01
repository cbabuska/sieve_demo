from libc.stdlib cimport free

cdef extern from "sieve_c_imp.c":
    struct PrimesStruct:
        int num_primes 
        int *primes
    
    PrimesStruct *get_primes_c(int max_num_to_consider)

def get_primes(int max_num_to_consider):
    cdef PrimesStruct *primes_struct = get_primes_c(max_num_to_consider)
    cdef i
    primes = []
    
    for i in range(0, primes_struct.num_primes):
        primes.append(primes_struct.primes[i])
    
    free(primes_struct.primes)
    free(primes_struct)

    return primes
