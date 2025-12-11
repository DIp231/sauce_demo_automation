@echo off
REM Batch script to run Sauce Demo automation tests
REM This script runs tests on Windows

echo.
echo ========================================
echo  SAUCE DEMO - AUTOMATION TEST RUNNER
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [INFO] Installing required dependencies...
pip install -r requirements.txt

echo.
echo [INFO] Creating necessary directories...
if not exist reports mkdir reports
if not exist screenshots mkdir screenshots
if not exist extracted_data mkdir extracted_data

echo.
echo ========================================
echo  Running Scenario 1: Successful Login
echo ========================================
echo.
python -m pytest tests/test_scenario_1.py -v --html=reports/scenario_1_report.html --self-contained-html -m scenario1

echo.
echo ========================================
echo  Running Scenario 2: Failed Login
echo ========================================
echo.
python -m pytest tests/test_scenario_2.py -v --html=reports/scenario_2_report.html --self-contained-html -m scenario2

echo.
echo ========================================
echo  Running Scenario 3: Extract Data
echo ========================================
echo.
python -m pytest tests/test_scenario_3.py -v --html=reports/scenario_3_report.html --self-contained-html -m scenario3

echo.
echo ========================================
echo  Running All Tests with Report
echo ========================================
echo.
python -m pytest tests/ -v --html=reports/full_test_report.html --self-contained-html --junit-xml=reports/junit_report.xml

echo.
echo ========================================
echo  Test Execution Complete!
echo ========================================
echo.
echo Reports generated in the 'reports' folder
echo Screenshots saved in the 'screenshots' folder
echo Extracted data saved in the 'extracted_data' folder
echo.
pause
