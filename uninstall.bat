@echo off
setlocal

:: Check if the virtual environment exists
if exist "aupe_env\Scripts\activate.bat" (
    :: Deactivate the virtual environment if it is currently active
    if not "%VIRTUAL_ENV%" == "" (
        echo Deactivating the virtual environment...
        deactivate
    )

    :: Uninstall all packages in the virtual environment
    echo Uninstalling all dependencies...
    call aupe_env\Scripts\pip.exe freeze > requirements.txt
    call aupe_env\Scripts\pip.exe uninstall -r requirements.txt -y

    :: Remove the virtual environment
    echo Deleting the virtual environment folder...
    rmdir /s /q aupe_env
) else (
    echo Virtual environment does not exist. Skipping uninstallation of dependencies...
)

:: Delete the remaining files
echo Deleting specified files...
del "Webserver-Merged.py" >nul 2>&1
del "Dashboard-Merged.py" >nul 2>&1

:: Delete the `requirements.txt` file if it exists
del "requirements.txt" >nul 2>&1

@REM :: Optional: Clean up the generated Python scripts
@REM echo Deleting any generated Python scripts...
@REM del "*.py" >nul 2>&1

:: Print completion message
echo Uninstallation complete. All specified files and folders have been deleted.
pause
