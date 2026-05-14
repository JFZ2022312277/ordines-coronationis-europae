@echo off
REM Restore index.html from backup
echo Restoring index.html from backup...
cd /d "C:\Users\32433\Desktop\Ordines Coronationis For Speculum"
copy /Y "index.html.bak-precleanup-20260514" "index.html"
echo.
echo Restoration complete!
echo.
echo Verifying file...
if exist "index.html" (
    for %%A in ("index.html") do (
        echo File size: %%~zA bytes
    )
    findstr "</html>" "index.html" >nul && echo File contains closing html tag: YES
) else (
    echo ERROR: File not found!
)
pause
