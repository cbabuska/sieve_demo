from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles = ['sieve.pyx']
ext_modules = [Extension('sieve', sourcefiles)]

setup(name='sieve',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules)
