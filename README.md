# helping_hand_tester
This project is aimed to make life easier for people in the Performance Engineering team.

## Setup instructions for developers
When you've cloned the repo. make sure to setup a virtualenv and use the requirements.txt file to install all dependencies:
```
pip install -r requirements.txt
```
The project has to be run from main.py.

Notice that one of the installations is pysinstaller. It let's us build our project into one executable file.
Running the following command will create a folder called dist wich contains the executable file.
```
pyinstaller -F main.py
```
