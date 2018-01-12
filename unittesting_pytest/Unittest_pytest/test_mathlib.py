import mathlib
import pytest

#@pytest.mark.skip(reason="Im skipping this test")
def test_cal_total():
	total=mathlib.calc_sum(4,5)
	assert total==9

def test_cal_mul():
    result=mathlib.calc_mul(2,6)
    assert result==12

@pytest.mark.wingroup
def test_window_1():
    assert True

@pytest.mark.wingroup
def test_window_2():
    assert True

@pytest.mark.macgroup
def test_mac_1():
    assert True

@pytest.mark.macgroup    
def test_mac_2():
    assert True

