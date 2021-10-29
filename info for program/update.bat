@echo off
taskkill /f /pid %1
python3.9 update.py