from src.main import greet


def test_greet():
    assert greet("Python") == "Hello, Python!"
    assert greet("World") == "Hello, World!"
    assert greet("") == "Hello, !"
