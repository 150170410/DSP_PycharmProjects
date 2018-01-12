import mathlib
import pytest

#----skip test cases------>>pytest -v -rsx
@pytest.mark.skip(reason="Im skipping this test")
def test_cal_total():
	total=mathlib.calc_sum(4,5)
	assert total==9

def test_cal_mul():
    result=mathlib.calc_mul(2,6)
    assert result==12

#---Group some testcases to run>> pytest -m wingroup -v
@pytest.mark.wingroup
def test_window_1():
    assert True

@pytest.mark.wingroup
def test_window_2():
    assert True
#---Group some testcases to run>> pytest -m macgroup -v
@pytest.mark.macgroup
def test_mac_1():
    assert True

@pytest.mark.macgroup
def test_mac_2():
    assert True

#---------Use fixture to access DB---------
import pytest
import cx_Oracle

@pytest.fixture(scope="module")
def cur():
        conn=cx_Oracle.connect('DSP/DSP@localhost/orcl')
        curs=conn.cursor()
        yield curs

        curs.close()
        conn.close()

def test_checlICCID(cur):
        iccid=cur.execute("select * from DSP_SIM_INVENTORY_DTLS where ICCID like '893144030170000198'")
        assert iccid==893144030170000198

def test_checlICCID(cur):
        imsi=cur.execute("select * from DSP_SIM_INVENTORY_DTLS where REAL_IMSI like '204041000000199'")
        assert imsi==204041000000199

#------------parametrize testcase using tupple-------------
import mathlib
import pytest

@pytest.mark.parametrize("in_value,out_value",[(2,4),(5,25),(7,49)])
def test_checkSqaure(in_value,out_value):
    result=mathlib.calc_sqaure(in_value)
    assert result==out_value
