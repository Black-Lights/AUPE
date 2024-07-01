@echo off
setlocal

:: Define the PIDs for the webserver and dashboard scripts
:: These will be assigned manually by the starting script or via environment variables
set "WEBAPP_PORT_1=5000"
set "WEBAPP_PORT_2=8050"

:: Find and kill the webserver process
echo Stopping webserver script on port %WEBAPP_PORT_1%...
for /f "tokens=2" %%a in ('netstat -ano ^| findstr :%WEBAPP_PORT_1%') do set webserver_pid=%%a
if defined webserver_pid (
    echo Killing webserver process ID %webserver_pid%
    taskkill /PID %webserver_pid% /F
) else (
    echo No webserver process found on port %WEBAPP_PORT_1%.
)

:: Find and kill the dashboard process
echo Stopping dashboard script on port %WEBAPP_PORT_2%...
for /f "tokens=2" %%a in ('netstat -ano ^| findstr :%WEBAPP_PORT_2%') do set dashboard_pid=%%a
if defined dashboard_pid (
    echo Killing dashboard process ID %dashboard_pid%
    taskkill /PID %dashboard_pid% /F
) else (
    echo No dashboard process found on port %WEBAPP_PORT_2%.
)

:: Delete the created Python scripts
echo Deleting generated Python scripts...
del "Webserver-Merged.py"
del "Dashboard-Merged.py"

:: Close the main command window
echo All processes stopped and files deleted. Press any key to exit.
pause >nul
exit