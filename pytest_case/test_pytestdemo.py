import pytest

def test_m2_01():
    print('这是 subpath1/test_module1.py::test_m1_1')
    assert 1==1

def test_demo1():
    assert 2 != 1


if __name__ == "__main__":
    pytest.main(['-v'])