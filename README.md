# gui_pyqt6_trial

This project demonstrates a minimal PyQt6 GUI trial.

Setup (Windows PowerShell)

1. Create virtual environment:

   Set-Location -Path 'C:\Users\bhara\Documents\GitHub\gui_pyqt6_trial'; python -m venv .venv

2. Activate (PowerShell):

   .\.venv\Scripts\Activate.ps1

   If activation is blocked, you can run the venv Python directly:

   .\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
   .\.venv\Scripts\python.exe -m pip install PyQt6

3. Save pinned dependencies:

   .\.venv\Scripts\python.exe -m pip freeze > requirements.txt

4. Quick verify:

   .\.venv\Scripts\python.exe -c "from PyQt6.QtCore import PYQT_VERSION_STR; print('PyQt6', PYQT_VERSION_STR)"

Notes

- The README includes commands for PowerShell. For cmd.exe use the corresponding activate script `\.venv\\Scripts\\activate.bat`.
- If you prefer a different venv name, update the commands accordingly.
