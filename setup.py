#!/usr/bin/env python
# coding: utf-8


try:
    # python setup.py test
    import multiprocessing
except ImportError:
    pass

import mistune
from setuptools import setup, Extension

try:
    from Cython.Distutils import build_ext
    cmdclass = {'build_ext': build_ext}
    ext_modules = [Extension('mistune', ['mistune.py'])]
except ImportError:
    cmdclass = {}
    ext_modules = []

# patch bdist_wheel
try:
    from wheel.bdist_wheel import bdist_wheel

    class _bdist_wheel(bdist_wheel):
        def get_tag(self):
            tag = bdist_wheel.get_tag(self)
            repl = 'macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64'
            if tag[2] == 'macosx_10_6_intel':
                tag = (tag[0], tag[1], repl)
            return tag

    cmdclass['bdist_wheel'] = _bdist_wheel
except ImportError:
    pass


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()

setup(
    name='mistune',
    version=mistune.__version__,
    url='https://github.com/lepture/mistune',
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    description='The fastest markdown parser in pure Python',
    long_description=fread('README.rst'),
    license='BSD',
    py_modules=['mistune'],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    zip_safe=False,
    platforms='any',
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Text Processing :: Markup',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
