@echo off
echo Backup completo...
set fecha=/15/ 1Mo_1813
set fecha= =0
powershell Compress-Archive -Path "C:\GWA_Studio_Core_GK\*" -DestinationPath "C:\GWA_BACKUP\GAB_IA_.zip" -Force
echo Backup en C:\GWA_BACKUP\
pause
