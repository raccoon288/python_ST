import pytest
from fixture.application import Application
import json
import os.path


fixture = None
target = None


@pytest.fixture()
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        abs_path = os.path.abspath(__file__)
        dir_name = os.path.dirname(abs_path)
        config_file = os.path.join(dir_name, request.config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(login=target["login"], password=target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
