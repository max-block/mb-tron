from decimal import Decimal

from mb_tron.tron import utils


def test_to_sun():
    assert utils.to_sun(1) == 1_000_000
    assert utils.to_sun(1.1) == 1_100_000
    assert utils.to_sun(Decimal("1.1")) == 1_100_000
