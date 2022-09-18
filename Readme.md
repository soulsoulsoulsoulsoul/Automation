# How to setup?
This script should be run in a separate workstation so that it doesn't interfere with other programs.
This project is created with Python3.8.10. It assumes it's already installed on your system.
Use the given steps to get it working:-
1. Run following command to create a virtual environment:-
```
python -m venv venv
```
It will create a virtual environment and creates a `/env` directory inside your project.
2. To activate the virtual environment, use
```
source env/bin/activate
```

3. Now, we need to install the neccessary dependencies. To do so, run the following command,
```
pip install -r requirements.txt
```

# How to run the automation?

To do so, open the project folder in your terminal, and run the following command:-
1.
```
source env/bin/activate
```

2. Run the automation
```
python3 base.py
```
Now you can switch to your main workstation and see the automation in action.

# Window is not switching for me?
It maybe happening due to different shortcut in your system, open `base.py` and edit it according to your shortcut:-
```python
def change_window(self):
  with pyautogui.hold('alt'):
    pyautogui.press('tab')
```
