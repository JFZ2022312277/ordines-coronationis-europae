@echo off
REM Windows convenience wrapper for serve.py.
REM Double-click this file to start the local preview server.
REM Requires Python 3 in PATH.

cd /d "%~dp0"
python serve.py
pause
