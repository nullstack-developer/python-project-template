from python_project import __version__, add


def test_version():
    assert __version__ == "0.1.0"


def test_add():
    first = 10
    second = 20
    assert add(first, second) == first + second
