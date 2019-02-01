#include <Python.h>

struct PrimesStruct
{
    int num_primes;
    int *primes;
};

struct PrimesStruct *get_primes_c(int max_num_to_consider)
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

static PyObject *wrap_c_api_sieve_get_primes(PyObject *self, PyObject *args)
{
    int max_num_to_consider;
    PyArg_ParseTuple(args, "i", &max_num_to_consider);

    struct PrimesStruct *primes = get_primes_c(max_num_to_consider);

    PyObject *python_list_of_primes = PyList_New(primes->num_primes);
    for (int i=0; i<primes->num_primes; i++)
    {
        PyObject *python_int = Py_BuildValue("i", primes->primes[i]);
        PyList_SetItem(python_list_of_primes, i, python_int);
    }

    return python_list_of_primes;
}

static PyMethodDef sieve_funcs[] =
{
    {"get_primes", (PyCFunction)wrap_c_api_sieve_get_primes, METH_VARARGS, ""}
};

static struct PyModuleDef sieve =
{
    PyModuleDef_HEAD_INIT,
    "wrap_c_api_sieve",
    "",
    -1,
    sieve_funcs
};

PyMODINIT_FUNC PyInit_wrap_c_api_sieve(void)
{
    return PyModule_Create(&sieve);
}
