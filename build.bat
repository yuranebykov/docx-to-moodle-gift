@echo off
echo Building .exe...

:: Name without quotes
set APP_NAME=docx-to-moodle-gift
set MAIN_FILE=app.py

:: Path to pyinstaller in .venv
set PYI=.venv\Scripts\pyinstaller.exe

:: Check if pyinstaller exists
if not exist %PYI% (
    echo Not found: %PYI%
    echo Try: pip install pyinstaller
    pause
    exit /b
)

:: Build
%PYI% ^
 --onefile ^
 --noconsole ^
 --name %APP_NAME% ^
 --icon=icon.ico ^
 --version-file=file_version.txt ^
 --add-data icon.ico;. ^
 %MAIN_FILE%

echo Done! Check dist\%APP_NAME%.exe
pause