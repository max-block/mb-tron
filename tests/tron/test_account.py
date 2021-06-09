from mb_tron.tron import account


def test_generate_account():
    acc1 = account.generate_account()
    acc2 = account.generate_account()
    assert acc1.address.startswith("T")
    assert acc2.address.startswith("T")
    assert acc1.address != acc2.address
    assert account.is_valid_address(acc1.address)
    assert account.is_valid_address(acc2.address)


def test_is_valid_address():
    assert account.is_valid_address("TXcoPj81sYLef7TrEjKsgqcX7M9z1TCkZL")
    assert not account.is_valid_address("TXcoPj81sYLef7TrEjKsgqcX7M9z1TCkZl")
    assert not account.is_valid_address("TXcoPj81sYLef7TrEjKsgqcX7M9z1TCkZ")


def test_get_address_from_private_key():
    private_key = "aaf2a3148255e466c7c924b1f4ba41b101f486622bf4bafd0b69a077d8cc83d3"
    assert account.get_address_from_private_key(private_key) == "TXcoPj81sYLef7TrEjKsgqcX7M9z1TCkZL"
