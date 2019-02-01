from distutils.core import setup, Extension

setup(name='wrap_c_api_sieve', 
      version='1.0', 
      ext_modules=[Extension('wrap_c_api_sieve', ['sieve.c'])])
