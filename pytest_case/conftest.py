import pytest


@pytest.fixture(scope='session')
def get_base_url():
    base_url = "http://22.144.101.183:13010/bpmService"
    print(base_url)
    return base_url
