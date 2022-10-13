import unittest
from lab import Rocket

class TestMylab(unittest.TestCase):
    def test_converter_correct(self):
        mass = 3700000
        for mass in[3700000,3800000]:
            obj = Rocket("Ares V", mass)
            self.assertAlmostEqual(obj.convert_mass(), mass * 2.20462262)

    def test_mock    
