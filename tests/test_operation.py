import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.math_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert add(5,3)==2
    assert add(4,3)==1
    assert add(3,3)==0
    assert add(2,3)==-1