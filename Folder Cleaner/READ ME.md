# File Cleaner Script

This Python script deletes files and folders from a specified directory if they are older than a certain number of days. By default, it checks for files older than 7 days and deletes them. 

## Prerequisites

- Python 3.x installed on your system
- The `shutil` module (included in the Python Standard Library)
- The `os` and `time` modules (included in the Python Standard Library)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Effaly/automation-mini-projects.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```

## Usage

1. Update the script with the path to your Downloads folder:
    ```python
    downloads_path = "C:\\Users\\USERNAME\\Downloads"  # Update this path
    ```

2. Run the script:
    ```bash
    python delete_old_files.py
    ```

## Automating the Script

### Example to Run Weekly:

#### If you're on Windows:

You can use Task Scheduler to run the script weekly:

1. Open Task Scheduler and create a new task.
2. Set the trigger to run the task weekly.
3. Set the action to start a program and point it to your Python interpreter, with the script file as an argument.

#### If you're on macOS or Linux:

You can use cron to run the script weekly:

1. Open the terminal and type `crontab -e` to edit the cron jobs.
2. Add a line to run the script weekly, for example:
    ```bash
    0 0 * * 0 /usr/bin/python3 /path/to/your_script.py
    ```
    This runs the script every Sunday at midnight.
