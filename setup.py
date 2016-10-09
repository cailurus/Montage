#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools.command.install import install
from setuptools import setup

with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()

class MakeCommand(install):
    def run(self):
        os.system('make')
        common_dir = 'tmontage/wumanber'
        target_dir = '%s/%s' % (self.build_lib, common_dir)
        self.mkpath(target_dir)
        os.system('cp %s/wumanber.so %s' %(common_dir, target_dir))
        install.run(self)

setup(
    name='tmontage',
    version='0.1.3',
    packages=['tmontage'],
    url='https://github.com/ailurus1991/Montage',
    license='GPL2',
    author='jinyang zhou',
    author_email='jinyang.zhou@guokr.com',
    description='A multipattern matching toolbox',
    long_description=LONG_DESCRIPTION,
    install_requires=[''],
    keywords='matching, multipattern matching',
    cmdclass={'install': MakeCommand}
)
