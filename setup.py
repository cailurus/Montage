#!/usr/bin/env python
# encoding: utf-8

from setuptools.command.install import install
from setuptools import setup


with open('README.md') as f:
    LONG_DESCRIPTION = f.read()


class MakeCommand(install):
    def run(self):
        install.run()

setup(
    name='',
    version='',
    packages=[''],
    url='',
    license='GPL2',
    author='jinyang',
    author_email='jinyang.zhou@guokr.com',
    description='',
    long_description=LONG_DESCRIPTION,
    install_requires=[''],
    keywords='',
    cmdclass={'install': MakeCommand}
)
