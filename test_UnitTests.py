
import python_hw5


def test_q1_bondInit():
    b1 = python_hw5.Bond(2e6, 0.03, 0.04, 10, 1)
    assert b1.face == 2e6
    assert b1.ytm == 0.03
    assert b1.couponrate == 0.04
    assert b1.m == 10
    assert b1.pmtperyear == 1


def test_q2_convertibleBondInit():
    cb1 = python_hw5.ConvertibleBond(2e6, 0.03, 0.04, 10, 1, 0.5)
    assert cb1.face == 2e6
    assert cb1.ytm == 0.03
    assert cb1.couponrate == 0.04
    assert cb1.m == 10
    assert cb1.pmtperyear == 1
    assert cb1.conversion_ratio == 0.5


def test_q3_num_bonds():
    cb1 = python_hw5.ConvertibleBond(2e6, 0.03, 0.04, 10, 1, 0.5)
    assert cb1.num_bonds == 2000


def test_q4_conversion_value():
    cb1 = python_hw5.ConvertibleBond(2e6, 0.03, 0.04, 10, 1, 0.5)
    assert cb1.getConversionValue(100) == 100000


def test_q4_conversion_price():
    cb1 = python_hw5.ConvertibleBond(2e6, 0.03, 0.04, 10, 1, 0.5)
    # asset ansewr close to 2170.61
    assert abs(cb1.getConversionPrice() - 2170.61) < 1e-2
