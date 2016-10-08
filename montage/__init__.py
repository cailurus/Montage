#!/usr/bin/env python
# encoding: utf-8


class MontageException(Exception):
    pass

class Montage(object):
    def __init__(self, name):
        self.name = name

    def __loadText__(self, text):
        pass
