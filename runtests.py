# coding: utf-8

import unittest
import shutil

from tmontage import Montage

class MontageTest(unittest.TestCase):
    def test_wm(self):
        wm_sample = Montage("sample")
        wm_sample.init_pattern(["hehe", "haha", "world"])
        result = wm_sample.search_text("hello,world.")
        assert result == {'world':[6]}

        shutil.rmtree("__pycache__")

if __name__ == 'main':
    unittest.main()
