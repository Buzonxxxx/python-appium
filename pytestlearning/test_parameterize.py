import pytest


def get_data():
    return [
        ("Louis@automation.com", "123445"),
        ("Lucas@automation.com", "saasfaf"),
        ("Levi@automation.com", "afasf"),
        ("Anney@automation.com", "xvxv"),
        ("Annie@automation.com", "213123"),
        ("Henry@automation.com", "gbbdsfs")
    ]


@pytest.mark.parametrize("username, password", get_data())
def test_login(username, password):
    print(f'username: {username}, password: {password}')
