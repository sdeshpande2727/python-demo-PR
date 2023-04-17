# src/tests/test_helloworld.py

from helloworld import hello


def test_hello():
    assert hello() == "Hello, world!"
