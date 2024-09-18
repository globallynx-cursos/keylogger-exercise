# Keylogger Project for Conference Presentation

This project is designed to demonstrate the basics of keylogging for educational purposes. Please use this responsibly and only in environments where you have permission to do so.

## Setup Instructions

### 1. Install Anaconda

First, download and install Anaconda from the official site: [Anaconda Download](https://www.anaconda.com/download).

### 2. Create an Anaconda Environment

After installing Anaconda, follow these steps to create a new environment:

- Open Anaconda Navigator.
- Go to the "Environments" tab.
- Click on "Create" at the bottom left.
- Name your environment (e.g., `keylogger_env`) and ensure Python 3 is selected.
- Click "Create".

### 3. Activate Environment and Open Terminal

Once the environment is created:

- Click on the green arrow next to your new environment.
- Select "Open Terminal" to launch a terminal in the context of the selected environment.

### Install Required Packages

In the terminal that opens, install the required packages using pip:

```bash
pip install flask
pip install pynput requests
pip install pyinstaller
```

## Running the Project
### Run the Server
Navigate to the server directory of the project, then start the Flask server by running:
```bash
python main.py
```

### Run the Client
Open a new terminal window, navigate to the client directory, and start the keylogger client with:

```bash
python main.py
```

### Creating the Executable for client
Run PyInstaller with Options: To create an executable for your main.py script without a console window, execute the following command:
```bash
pyinstaller --onefile --noconsole main.py
```

`--onefile`: Tells PyInstaller to bundle everything into a single executable. The output will be larger but will contain all the necessary dependencies.

`--noconsole`: This option hides the console window when running the executable, which is particularly useful for applications that do not need to display a command prompt


## Notes
The server component collects and stores keystroke data sent from the client.
The client component monitors and logs keystrokes, sending them to the server upon a specific trigger (e.g., pressing the ESC key).
Use PyInstaller to create an executable for the client if needed, allowing for easier distribution and execution.

## Disclaimer
This project is intended for educational purposes only and should not be used maliciously or to infringe on anyone's privacy. Always obtain explicit permission before using keylogging software in any environment.

## TODO 
Requirements