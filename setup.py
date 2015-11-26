import os
from setuptools import setup


def read(filename):
    return open(os.path.join(__file__, filename)).read()
    

setup(
    name='gitignorepy',
    version='0.1.0',
    description='cli to create gitignore files from gitignore.io',
    long_description=read('readme.md'),
    keywords='cli gitignore git',
    url='https://github.com/jedijulia/gitignorepy',
    author='Julia Menchavez',
    author_email='jcmenchavez@gmail.com',
    license='MIT',
    packages=['gitignorepy'],
    scripts=['bin/gitignorepy'],
    install_requires=['requests'],
    setup_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'])
