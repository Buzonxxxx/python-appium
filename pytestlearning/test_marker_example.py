import pytest


@pytest.mark.functional
def test_do_login():
    print('execute login test')


@pytest.mark.regression
def test_user_reg():
    print('execute user reg test')


@pytest.mark.functional
def test_compose_email():
    print('execute compose email test')


@pytest.mark.skip
def test_skip():
    print('skipping test')
