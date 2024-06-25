import pytest


def test_addition():
    assert 2 + 2 == 1


@pytest.mark.smoke
def test_addition2():
    assert 2 + 2 == 4


@pytest.mark.smoke
def test_addition3():
    assert 2 + 2 == 4


@pytest.mark.skip(reason="Not Implemented Yet")
def test_addition4():
    assert 5 + 2 == 7
