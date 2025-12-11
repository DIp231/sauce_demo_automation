#!/bin/bash
# Shell script to run Sauce Demo automation tests
# This script runs tests on Linux/macOS

echo ""
echo "========================================"
echo " SAUCE DEMO - AUTOMATION TEST RUNNER"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed or not in PATH"
    exit 1
fi

echo "[INFO] Installing required dependencies..."
pip install -r requirements.txt

echo ""
echo "[INFO] Creating necessary directories..."
mkdir -p reports
mkdir -p screenshots
mkdir -p extracted_data

echo ""
echo "========================================"
echo " Running Scenario 1: Successful Login"
echo "========================================"
echo ""
python -m pytest tests/test_scenario_1.py -v --html=reports/scenario_1_report.html --self-contained-html -m scenario1

echo ""
echo "========================================"
echo " Running Scenario 2: Failed Login"
echo "========================================"
echo ""
python -m pytest tests/test_scenario_2.py -v --html=reports/scenario_2_report.html --self-contained-html -m scenario2

echo ""
echo "========================================"
echo " Running Scenario 3: Extract Data"
echo "========================================"
echo ""
python -m pytest tests/test_scenario_3.py -v --html=reports/scenario_3_report.html --self-contained-html -m scenario3

echo ""
echo "========================================"
echo " Running All Tests with Report"
echo "========================================"
echo ""
python -m pytest tests/ -v --html=reports/full_test_report.html --self-contained-html --junit-xml=reports/junit_report.xml

echo ""
echo "========================================"
echo " Test Execution Complete!"
echo "========================================"
echo ""
echo "Reports generated in the 'reports' folder"
echo "Screenshots saved in the 'screenshots' folder"
echo "Extracted data saved in the 'extracted_data' folder"
echo ""
