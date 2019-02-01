#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct PrimesStruct
{
    int num_primes;
    int *primes;
};

struct PrimesStruct *get_primes(int max_num_to_consider)
{
    struct PrimesStruct *primes = malloc(sizeof(struct PrimesStruct));

    if (max_num_to_consider < 2)
    {
        primes->num_primes = 0;
        primes->primes = malloc(sizeof(int) * 0);
        return primes;
    }

    char is_prime_list[max_num_to_consider+1];
    memset(is_prime_list, 1, max_num_to_consider+1);
    primes->num_primes = 0;

    for (int i=2; i<max_num_to_consider+1; i++)
    {
        if (is_prime_list[i] == 0)
        {
            continue;
        }  

        primes->num_primes = primes->num_primes + 1;
        
        for (int j=i+1; j<max_num_to_consider+1; j++)
        {
            if (is_prime_list[j] == 0)
            {
                continue;
            } 
            if (j % i == 0)
            {
                is_prime_list[j] = 0;
            }
        }
    }

    primes->primes = malloc(sizeof(int) * primes->num_primes);
    
    int prime_counter = 0;
    for (int i=2; i<max_num_to_consider+1; i++)
    {
        if (is_prime_list[i] == 1)
        {
            primes->primes[prime_counter++] = i;
        }
    }
    
    return primes;
}

void free_primes_struct(struct PrimesStruct *primes)
{
    free(primes->primes);
    free(primes);
}
