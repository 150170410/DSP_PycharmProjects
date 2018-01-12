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

