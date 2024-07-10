@echo off

:: Check if the virtual environment already exists
if not exist "aupe_env\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv aupe_env
) else (
    echo Virtual environment already exists. Skipping creation...
)

:: Activate the virtual environment
call aupe_env\Scripts\activate

:: Upgrade pip
python -m pip install --upgrade pip

:: Install required packages
python -m pip install -r requirements.txt

echo Environment setup complete. To start the web app, run AUPE_RiskMointor.bat
pause

