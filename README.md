# Sauce Demo Automation Tests

This project contains automated test cases for the Sauce Demo web application (https://www.saucedemo.com/).

## Overview

This automation suite validates three scenarios:
1. **Scenario 1**: Successful Login - Validates that a standard user can login successfully
2. **Scenario 2**: Failed Login - Validates error handling for locked out users
3. **Scenario 3**: Extract Data - Validates data extraction from inventory and logout functionality

## Project Structure

```
sauce_demo_automation/
├── config/
│   ├── __init__.py
│   └── settings.py              # Configuration settings
├── pages/
│   ├── __init__.py
│   ├── base_page.py            # Base page object class
│   ├── login_page.py           # Login page object
│   └── inventory_page.py       # Inventory page object
├── tests/
│   ├── __init__.py
│   ├── test_scenario_1.py      # Test case for successful login
│   ├── test_scenario_2.py      # Test case for failed login
│   └── test_scenario_3.py      # Test case for data extraction
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py       # WebDriver factory
│   ├── logger_config.py        # Logger configuration
│   └── screenshot_helper.py    # Screenshot utility
├── conftest.py                 # Pytest configuration and fixtures
├── pytest.ini                  # Pytest settings
├── requirements.txt            # Python dependencies
├── run_tests.bat              # Windows batch script
├── run_tests.sh               # Linux/macOS shell script
└── README.md                  # This file
```

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone or download the project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Using the Automated Scripts

**On Windows:**
```bash
run_tests.bat
```

**On Linux/macOS:**
```bash
bash run_tests.sh
```

### Using pytest directly

**Run all tests:**
```bash
pytest tests/ -v
```

**Run specific scenario:**
```bash
# Scenario 1
pytest tests/test_scenario_1.py -v -m scenario1

# Scenario 2
pytest tests/test_scenario_2.py -v -m scenario2

# Scenario 3
pytest tests/test_scenario_3.py -v -m scenario3
```

**Run with custom markers:**
```bash
# Run all login-related tests
pytest tests/ -v -m login

# Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html
```

**Run tests in parallel:**
```bash
pytest tests/ -v -n auto
```

## Test Scenarios

### Scenario 1: Successful Login
**File:** `tests/test_scenario_1.py`

**Test Case:** `test_successful_login`

**Steps:**
1. Navigate to the login page
2. Enter standard user credentials (username: "standard user", password: "secret sauce")
3. Click the login button
4. Verify successful redirect to inventory page
5. Verify app logo is visible

**Expected Result:** User is successfully logged in and redirected to inventory page

---

### Scenario 2: Failed Login (Locked Out User)
**File:** `tests/test_scenario_2.py`

**Test Case:** `test_failed_login_locked_out_user`

**Steps:**
1. Navigate to the login page
2. Enter locked out user credentials (username: "locked_out_user", password: "secret_sauce")
3. Click the login button
4. Verify error message is displayed
5. Verify error message contains "Sorry, this user has been banned."

**Expected Result:** Login fails with appropriate error message, user remains on login page

---

### Scenario 3: Extract and Save Inventory Data
**File:** `tests/test_scenario_3.py`

**Test Case:** `test_extract_and_save_inventory_data`

**Steps:**
1. Login with standard user credentials
2. Navigate to inventory page
3. Extract product data (name, description, price)
4. Save extracted data in multiple formats:
   - JSON format
   - CSV format
   - TXT format
5. Logout from the application
6. Verify redirect to login page

**Expected Result:** Data is successfully extracted and saved in multiple formats, user is logged out

---

## Generated Reports

After running tests, the following reports are generated:

1. **HTML Reports**
   - `reports/scenario_1_report.html` - Scenario 1 test report
   - `reports/scenario_2_report.html` - Scenario 2 test report
   - `reports/scenario_3_report.html` - Scenario 3 test report
   - `reports/full_test_report.html` - Combined test report

2. **JUnit Report**
   - `reports/junit_report.xml` - JUnit format report

3. **Logs**
   - `reports/logs/automation_tests.log` - Detailed execution logs

4. **Screenshots**
   - `screenshots/` - Screenshots captured during test execution

5. **Extracted Data**
   - `extracted_data/inventory_data_*.json` - Extracted inventory data in JSON format
   - `extracted_data/inventory_data_*.csv` - Extracted inventory data in CSV format
   - `extracted_data/inventory_data_*.txt` - Extracted inventory data in text format

## Test Markers

The project uses pytest markers for selective test execution:

- `@pytest.mark.scenario1` - Marks tests for Scenario 1
- `@pytest.mark.scenario2` - Marks tests for Scenario 2
- `@pytest.mark.scenario3` - Marks tests for Scenario 3
- `@pytest.mark.login` - Marks tests related to login functionality

## Configuration

Configuration settings are stored in `config/settings.py`:

- **BASE_URL**: Application base URL
- **BROWSER_NAME**: Browser to use (default: chrome)
- **HEADLESS_MODE**: Run browser in headless mode (default: False)
- **IMPLICIT_WAIT**: Implicit wait timeout in seconds (default: 10)
- **EXPLICIT_WAIT**: Explicit wait timeout in seconds (default: 15)
- **TEST_USERS**: Test user credentials
- **BANNED_USER_ERROR_MESSAGE**: Expected error message for banned users
- **REPORT_FOLDER**: Folder for test reports
- **SCREENSHOTS_FOLDER**: Folder for screenshots
- **EXTRACTED_DATA_FOLDER**: Folder for extracted data

## Fixtures

The project uses pytest fixtures defined in `conftest.py`:

1. **driver** - Provides WebDriver instance for each test
2. **screenshot_on_failure** - Takes screenshot on test failure
3. **log_test_info** - Logs test information

## Page Objects

### BasePage
Base class for all page objects with common functionality:
- Element finding and interaction
- Waits for elements
- Text extraction
- URL navigation

### LoginPage
Page object for login page:
- `load()` - Navigate to login page
- `enter_username(username)` - Enter username
- `enter_password(password)` - Enter password
- `click_login_button()` - Click login button
- `login_user(username, password)` - Complete login
- `get_error_message()` - Get error message text
- `is_error_message_present()` - Check if error message exists
- `is_login_page_loaded()` - Verify login page is loaded

### InventoryPage
Page object for inventory page:
- `is_inventory_page_loaded()` - Check if inventory page is loaded
- `is_app_logo_visible()` - Check if app logo is visible
- `get_all_products()` - Extract all product data
- `logout()` - Logout from application

## Logging

Logs are automatically generated during test execution:
- Console output with test progress
- File logs in `reports/logs/automation_tests.log`
- Detailed logging of all interactions

## Error Handling

The framework includes comprehensive error handling:
- Custom exceptions for element not found
- Retry mechanisms for flaky operations
- Screenshot capture on failures
- Detailed error logs

## Browser Support

Currently supports:
- Google Chrome (default)
- Can be extended to support Firefox, Edge, Safari

## Known Issues and Limitations

None at this time.

## Future Enhancements

1. Add support for multiple browsers
2. Implement parallel execution
3. Add visual regression testing
4. Integrate with CI/CD pipelines
5. Add performance testing
6. Implement behavior-driven testing with Behave

## Contributing

When modifying or extending this project:
1. Follow PEP 8 style guidelines
2. Add appropriate logging statements
3. Update documentation
4. Include test cases for new features

## Support

For issues or questions, please refer to the test execution logs in `reports/logs/automation_tests.log`.

## Acknowledgments

This automation framework is built using:
- Selenium WebDriver for browser automation
- Pytest for test framework
- Python 3.8+

## License

This project is provided as is for testing purposes.
