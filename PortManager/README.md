# Port Manager

Port Manager is a Python-based GUI tool that helps users monitor and manage open network ports on their Windows system. It provides an interface to view open ports, identify associated services, and terminate processes that are using specific ports.

## Features

- **View Open Ports**: Displays a list of currently open ports with details including local and foreign addresses, connection state, process ID (PID), and associated service.
- **Close Ports**: Allows users to terminate processes associated with open ports using a single button click.
- **Service Identification**: Fetches and displays service details related to a process using preloaded CSV files.
- **Admin Privileges Check**: Ensures the application runs with administrator privileges for necessary permissions.

## Requirements

- Windows OS
- Python 3.x

## Installation

1. Clone or download the repository.
2. Ensure you have Python installed. You can check by running:
    ```sh
    python --version
    ```

## Usage

Run the script with administrative privileges:
```sh
python portManager.py
```
If not run as administrator, the script will automatically attempt to restart with elevated privileges.

Use the GUI buttons to:
- **Get Open Ports**: Retrieve a list of active network connections.
- **Close Application**: Exit the program.
- **Close Port**: Terminate the process associated with a specific open port.

## File Structure

### CSV File Format

The tool relies on two CSV files located in the `resources/` folder:

#### tcp.csv
| port | description |
|------|-------------|
| 80   | HTTP        |
| 443  | HTTPS       |

#### windows.csv
| Executable Name | Type   | Description            |
|-----------------|--------|------------------------|
| svchost.exe     | System | Windows Host Process   |

Make sure these files exist in the correct directory to enable service identification.

Feel free to add to these files to make them more exhaustive.

## Notes

- The tool uses `netstat -ano` to fetch open ports and `taskkill` to terminate processes.
- Running the application as an administrator is required for full functionality.
- If any CSV file is missing, a warning message will be displayed.

Feel free to contribute or suggest improvements!
