"""
Pytest configuration and fixtures
"""
import pytest
import os
import sys
from datetime import datetime
from utils.driver_factory import DriverFactory
from utils.logger_config import setup_logger
from utils.screenshot_helper import ScreenshotHelper
from config.settings import SCREENSHOTS_FOLDER

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logger = setup_logger(__name__)


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on (default: chrome)"
    )


def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line("markers", "scenario1: Mark test as scenario 1 (successful login)")
    config.addinivalue_line("markers", "scenario2: Mark test as scenario 2 (failed login)")
    config.addinivalue_line("markers", "scenario3: Mark test as scenario 3 (extract data)")
    config.addinivalue_line("markers", "login: Tests related to login functionality")


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture to create and destroy WebDriver instance
    
    Args:
        request: Pytest request object
        
    Yields:
        WebDriver: WebDriver instance
    """
    logger.info("=" * 80)
    logger.info(f"Starting test: {request.node.name}")
    logger.info("=" * 80)
    
    # Create driver
    driver = DriverFactory.create_driver()
    
    yield driver
    
    # Cleanup
    logger.info(f"Ending test: {request.node.name}")
    DriverFactory.quit_driver(driver)
    logger.info("=" * 80)


@pytest.fixture(scope="function")
def screenshot_on_failure(driver, request):
    """
    Fixture to take screenshot on test failure
    
    Args:
        driver: WebDriver instance
        request: Pytest request object
    """
    yield
    
    # If test failed, take screenshot
    if request.node.rep_call.failed if hasattr(request.node, 'rep_call') else False:
        screenshot_path = ScreenshotHelper.take_screenshot(driver, request.node.name)
        logger.info(f"Screenshot saved: {screenshot_path}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def log_test_info(request):
    """Auto-use fixture to log test information"""
    logger.info(f"\nTest: {request.node.name}")
    logger.info(f"Module: {request.node.module.__name__}")
    
    yield
    
    # Log test status
    if hasattr(request.node, 'rep_call'):
        status = "PASSED" if request.node.rep_call.passed else "FAILED"
        logger.info(f"Test Status: {status}\n")


# Custom markers for parallel execution
def pytest_collection_modifyitems(config, items):
    """Modify test items for custom markers"""
    for item in items:
        # Add markers based on test file
        if "test_scenario_1" in str(item.fspath):
            item.add_marker(pytest.mark.scenario1)
            item.add_marker(pytest.mark.login)
        elif "test_scenario_2" in str(item.fspath):
            item.add_marker(pytest.mark.scenario2)
            item.add_marker(pytest.mark.login)
        elif "test_scenario_3" in str(item.fspath):
            item.add_marker(pytest.mark.scenario3)
