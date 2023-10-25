import pytest


@pytest.fixture(scope='module')
def setupDB():
    print("Creating DB connection")

    yield
    print("Closing DB connection")


@pytest.fixture(scope='function')
def browser():
    print('launching browser')

    yield
    print('closing the browser')


# def test_do_login(setupDB, browser):
#     print('execute login test')
#
#
# def test_user_reg(setupDB, browser):
#     print('execute user reg test')

@pytest.mark.usefixtures("setupDB", "browser")
def test_do_login():
    print('execute login test')


@pytest.mark.usefixtures("setupDB", "browser")
def test_user_reg():
    print('execute user reg test')
