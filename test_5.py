"""
from programa import suma

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 5) == 4
"""

from programa import area_circulo
import math

def test_area_circulo():
    assert round(area_circulo(1), 2) == round(math.pi, 2)
    assert round(area_circulo(2), 2) == round(4 * math.pi, 2)