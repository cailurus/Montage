#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools.command.install import install
from setuptools import setup


with open('README.md') as f:
    LONG_DESCRIPTION = f.read()


class MakeCommand(install):
    def run(self):
        os.system('make')
        common_dir = 'rmontage/wumanber'
        target_dir = '%s/%s' % (self.build_lib, common_dir)
        self.mkpath(target_dir)
        print common_dir, "ccc"
        print target_dir, "ttt"
        os.system('cp %s/wumanber.so %s' %(common_dir, target_dir))
        print 'cp %s/wumanber.so %s' %(common_dir, target_dir+'/')



        install.run(self)

setup(
    name='rmontage',
    version='0.0.1',
    packages=['rmontage'],
    url='www.guokr.com',
    license='GPL2',
    author='jinyang',
    author_email='jinyang.zhou@guokr.com',
    description='',
    long_description=LONG_DESCRIPTION,
    install_requires=[''],
    keywords='',
    cmdclass={'install': MakeCommand}
)
