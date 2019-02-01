# Implements the sieve of eratoshenes
def get_primes(max_num_to_consider):
    primes = []
    possible_primes = list(range(2, max_num_to_consider+1));

    for candidate_prime in range(2, max_num_to_consider+1):
        if candidate_prime not in possible_primes:
            continue

        primes.append(candidate_prime)
        possible_primes = [x for x in possible_primes if x % candidate_prime != 0]
    
    return primes
