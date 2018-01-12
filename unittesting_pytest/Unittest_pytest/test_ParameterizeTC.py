import mathlib
import pytest

@pytest.mark.parametrize("in_value,out_value",[(2,4),(5,25),(7,49)])
def test_checkSqaure(in_value,out_value):
    result=mathlib.calc_sqaure(in_value)
    assert result==out_value
