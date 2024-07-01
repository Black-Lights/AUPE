@echo off

:: Activate the virtual environment
call aupe_env\Scripts\activate

:: Convert Jupyter notebooks to Python scripts (if not done already)
echo Converting notebooks to Python scripts...
aupe_env\Scripts\jupyter nbconvert --to script Webserver-Merged.ipynb
aupe_env\Scripts\jupyter nbconvert --to script Dashboard-Merged.ipynb

:: Run the webserver script
echo Running webserver script...
start "" /B python Webserver-Merged.py

:: Wait for the webserver to start up
timeout /t 5 /nobreak >nul

:: Run the dashboard script
echo Running dashboard script...
start "" /B python Dashboard-Merged.py

:: Open the browser with the Dash app
echo Opening the browser...
start "" http://127.0.0.1:8050