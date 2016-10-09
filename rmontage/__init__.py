#!/usr/bin/env python
# encoding: utf-8

from wm import WuManber

class MontageException(Exception):
    pass

class Montage(object):
    def __init__(self, name):
        self.name = name
        self.model = None

    def init_pattern(self, keys):
        self.model = WuManber(keys)
        return True

    def search_text(self, text):
        self.model.search_text(text)
        result = {}
        for k,v in self.model.keydict.iteritems():
            if v != []:
                result[self.model.keywords[k]] = self.model.keydict[k]

        return result

