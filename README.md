# Fun Time Tools

Welcome to the Fun Time Tools project! This repository contains a collection of useful Python-based tools for different tasks. Currently, it includes the following two subprojects:

- **Metadata Extractor Tool**: Extracts metadata from a variety of file types, including images, PDFs, and MS Word files.
- **IP Geolocation Tool**: Allows batch processing of IP addresses to retrieve their geolocation information.
- **Port Manager**: A GUI tool to monitor and manage open network ports on Windows systems.

## Features

### Metadata Extractor Tool

- **Images**: Extract metadata from JPEG images (EXIF data like camera model, date taken, etc.).
- **PDFs**: Extract metadata such as author, title, producer, and subject.
- **Text Files**: Extract metadata like word count, line count, and file encoding.
- Returns metadata in a structured CSV format.

### IP Geolocation Tool

- Perform geolocation lookups for single or multiple IP addresses.
- Batch processing of IP addresses from a text file.
- Output results in CSV.
- Uses ipinfo.io API for retrieving geolocation data.

### Port Manager

- View Open Ports: Displays a list of currently open ports with details including local and foreign addresses, connection state, process ID (PID), and associated service.
- Close Ports: Allows users to terminate processes associated with open ports using a single button click.
- Service Identification: Fetches and displays service details related to a process using preloaded CSV files.
- Admin Privileges Check: Ensures the application runs with administrator privileges for necessary permissions.

## Installation

To get started, you'll need to clone the repository and install the required dependencies.

Clone the repository:

```bash
git clone https://github.com/JakeHamacher/Fun-Time-Tools.git
```

Navigate to the project folder:

```bash
cd Fun-Time-Tools
```

Follow the specific installation instructions for each subproject in their own README.

## Contributing

Feel free to fork this repository and contribute improvements, bug fixes, or new features via pull requests. If you have any ideas or suggestions, don't hesitate to open an issue!
