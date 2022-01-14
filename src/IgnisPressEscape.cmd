@echo off
:loop
:loop
    call "%~dp0../bin/python/python.exe" "%~dp0main.py" %*
goto loop

