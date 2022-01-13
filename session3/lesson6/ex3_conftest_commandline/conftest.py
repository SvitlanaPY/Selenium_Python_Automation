# If you need to provide more detailed error messages, you can use the type parameter and raise pytest.UsageError:

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt",
        action="store",
        default="type1",
        help="my option: type1 or type2",
        type=type_checker,
    )


def type_checker(value):
    msg = "cmdopt must specify a numeric type as typeNNN"
    if not value.startswith("type"):
        raise pytest.UsageError(msg)
    try:
        int(value[4:])
    except ValueError:
        raise pytest.UsageError(msg)
    return value


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
