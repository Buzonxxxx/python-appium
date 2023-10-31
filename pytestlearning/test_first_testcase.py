def setup_module(module):
    print("creating DB connection")


def teardown_module(module):
    print("Closing DB connection")


def setup_function(function):
    print('launching browser')


def teardown_function(function):
    print('closing the browser')


def test_do_login():
    print('execute login test')


def test_user_reg():
    print('execute user reg test')
