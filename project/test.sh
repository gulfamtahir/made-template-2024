#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 >/dev/null 2>&1; then
    echo "Pipeline needs Python 3 but it's not installed."
    exit 1
fi

# Install required Python packages
python3 -m pip install -r project/requirements.txt

# Ensure pytest is installed
if ! python3 -m pytest --version >/dev/null 2>&1; then
    echo "Installing pytest..."
    python3 -m pip install pytest
fi

# Run the ETL pipeline
echo "Running ETL pipeline..."
python3 project/pipeline.py

# Checkin if our ETL pipeline running perfectly or not
if [ $? -ne 0 ]; then
    echo "ETL pipeline failed. Skipping tests."
    exit 1
fi

# Run the all the tests of our project
echo "Running test cases..."
pytest project/test.py

exit 0