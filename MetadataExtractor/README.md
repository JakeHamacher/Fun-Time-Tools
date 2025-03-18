# Metadata Extractor Tool

This tool provides a one-stop solution for extracting metadata from various file formats, including images, PDFs, and text files. It supports the following features:

- Image metadata extraction (JPEG): EXIF data like camera model, date taken, etc.
- PDF metadata extraction: Author, producer, title, and subject.
- Text file metadata extraction: Word count, line count, and file encoding.
- MIME type identification for files.

## Features

- Extracts metadata from the following file types:
    - **Images**: JPEG, including EXIF data.
    - **PDFs**: Extracts author, producer, title, and subject.
    - **Text files**: Word count, line count, and file encoding.
- Returns metadata in a structured format.
- Supports both local file paths and remote URLs for file input.

## Installation

To use this tool, you'll need to install the required dependencies.

1. Clone this repository:
        ```bash
        git clone https://github.com/JakeHamacher/Fun-Time-Tools.git
        ```

2. Navigate to the project folder:
        ```bash
        cd Fun-Time-Tools\metadata-extractor
        ```

3. Install the dependencies using pip:
        ```bash
        pip install -r requirements.txt
        ```

## Usage

You can use the tool by running the Python script directly with a file path as an argument.

### Command Line Usage

To extract metadata from a file, run the following command:

```bash
python metadata_extractor.py <file_path>
```

Replace `<file_path>` with the actual path to the file you want to extract metadata from.

#### Example

To extract metadata from a JPEG image:

```bash
python metadata_extractor.py /path/to/image.jpg
```

This will print the metadata extracted from the image.

### Supported File Types

- **Images**: Images (.jpg, .jpeg, .tiff)
    - Metadata: Camera model, date taken, GPS coordinates.
- **PDFs**: PDF (.pdf)
    - Metadata: Author, title, producer, subject.
- **Text Files**: Word Documents (.docx)
    - Metadata: Word count, line count.

### Output

The extracted metadata will be output in a csv file by default.

## Requirements

- Python 3.x
- External libraries:
    - `exifread` for extracting EXIF metadata from images.
    - `PyPDF2` for extracting metadata from PDF files.
    - `python-magic` for determining MIME types of files.

You can install the required dependencies using:

```bash
pip install -r requirements.txt
```
