@echo on
setlocal

REM Set the directory path
set "directory=%~1"

REM Check if the directory exists
if not exist "%directory%" (
    echo Directory does not exist.
    exit /b
)

REM Change to the specified directory
cd /d "%directory%"

REM Display the available Python files
echo Available Python files in %directory%:
setlocal enabledelayedexpansion
set "count=0"
for %%F in (*.py) do (
    set /a "count+=1"
    echo !count!. %%F
)

REM Prompt for user input
set /p "choice=Enter the number corresponding to the Python file you want to execute: "

REM Validate user input
set "counts=0"
echo !counts! hello
set "python_file="
for /f "tokens=1,* delims=." %%A in ('dir /b /a-d *.py') do (
    set /a "counts+=1"
    if !counts! equ %choice% (
        set "python_file=%%A.%%B"
        echo %python_file%
        python "%python_file%"
        exit /b
    )
)

REM Invalid choice
echo Invalid choice.
exit /b

REM Execute the chosen Python file
