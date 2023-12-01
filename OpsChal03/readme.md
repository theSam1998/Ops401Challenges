# Uptime Sensor Tool

## Introduction
This Uptime Sensor Tool is designed to monitor the status of a specified host and send email notifications in case of status changes. For security and ease of use, this script uses environment variables for email credentials.

## Setup Instructions

### Step 1: Set Up Environment Variables
Before running the script, you need to set up environment variables for your email credentials. This keeps your email information secure and out of the script itself.

#### For Unix/Linux/macOS:
1. Open your terminal.
2. Edit your shell profile file (e.g., `.bashrc`, `.zshrc`). You can do this with a text editor. For example, using nano: `nano ~/.bashrc`
3. Add the following lines at the end of the file (replace `your_email@gmail.com` and `your_password` with your actual Gmail address and password):
    - export BURNER_EMAIL_ADDRESS='your_email@gmail.com'
    - export BURNER_EMAIL_PASSWORD='your_password'
4. Save the file and exit the editor.
5. Apply the changes with the command: `source ~/.bashrc` (or `source ~/.zshrc` if using Zsh).

#### For Windows:
1. Press `Win + R`, type `sysdm.cpl`, and press Enter.
2. Go to the `Advanced` tab and click `Environment Variables`.
3. Under `User variables`, click `New` to create a new variable.
4. Enter `BURNER_EMAIL_ADDRESS` as the variable name and your Gmail address as the value.
5. Repeat the process to add another variable named `BURNER_EMAIL_PASSWORD` with your Gmail password as the value.
6. Click OK to close all dialog boxes.

### Step 2: Running the Script
With your environment variables set, you can now run the script.

1. Open your terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using Python: `python script_name.py` (replace `script_name.py` with the actual name of the script).
4. Follow the on-screen prompts to enter the necessary information, such as the host to monitor and the duration for monitoring.

## Usage Notes
- The script will automatically use the Gmail credentials set in your environment variables for sending email notifications.
- Ensure you have Python installed on your system to run this script.
- If you encounter any issues with sending emails, verify that your Gmail credentials are correct and that your Gmail account allows access via less secure apps.