import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        path = "C:\\Users\\durap\\Downloads\\chromedriver\\chromedriver.exe"
        service_obj = Service(executable_path=path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("window-size=1920x1080")
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser == "firefox":
        path = "C:\\Users\\durap\\Downloads\\geckodriver\\geckodriver.exe"
        service_obj = Service(executable_path=path)  # invoke the service object
        # options = webdriver.FirefoxOptions()
        # options = webdriver.FirefoxOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Firefox(service=service_obj, options=options)
        # options.add_argument("--window-size=1920x1080")
        driver = webdriver.Firefox(service=service_obj)
    else:
        path = "C:\\Users\\durap\\Downloads\\edgedriver\\msedgedriver.exe"
        service_obj = Service(executable_path=path)  # invoke the service object
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("window-size=1200x600")
        driver = webdriver.Edge(service=service_obj, options=options)
    return driver


def pytest_addoption(parser):  # this will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")

# pytest html report

# It is a hook for adding environment info to HTML report


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Suraj'

# It is a hook for delete/,odify environment info to HTML Report


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



