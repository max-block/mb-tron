from mb_tron.tron import trc20


def test_get_balance():
    balance = trc20.get_balance(trc20.USDT_TOKEN_ADDRESS, "TAUN6FwrnwwmaEqYcckffC7wYmbaS6cBiX")  # nosec
    assert balance.ok > 1_000_000
