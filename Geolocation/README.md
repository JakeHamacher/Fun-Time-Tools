
# IP Geolocation Tool

This is a Python-based command-line tool for batch geolocation lookups of IP addresses. It retrieves geolocation information (such as city, region, country, and more) for a given IP address or list of IP addresses. The results can be exported as a CSV.

## Features
- Geolocation lookup for single or multiple IP addresses
- Batch processing using an input file containing a list of IPs
- Output in CSV
- Command-line interface with configurable options

## Installation

### Prerequisites
- Python 3.6 or higher
- `requests` library (for API calls)
- `argparse` library (for command-line argument parsing)

### Steps
1. Clone the repository or download the source files.
2. Install the required Python dependencies using `pip`.

```bash
pip install -r requirements.txt
```

3. Obtain an API token for IP geolocation (e.g., from [ipinfo.io](https://ipinfo.io/)). Save it as `API_TOKEN` in the `config.py` file or configure it in your environment variables.

## Usage

### Command-Line Interface

You can use the script `ip_geoloc.py` to perform geolocation lookups.

#### Single IP Address Lookup:
You can provide a single IP address as an argument.

```bash
python3 ip_geoloc.py 8.8.8.8
```

#### Multiple IP Addresses Lookup:
You can provide multiple IP addresses as arguments.

```bash
python3 ip_geoloc.py 8.8.8.8 1.1.1.1 9.9.9.9
```

#### Using an Input File:
Alternatively, you can specify a text file containing a list of IPs to look up using the `--input-file` option.

```bash
python3 ip_geoloc.py --input-file ips.txt
```

Where `ips.txt` contains one IP address per line.

Example:
```
8.8.8.8
1.1.1.1
```

#### Output Options:
By default, the output will be written to a CSV file (`output.csv`). You can change the output format by specifying one of the following options:

For example, to output in JSON format:

```bash
python3 ip_geoloc.py --input-file ips.txt --output output.csv
```

### Batch Processing

You can also process a large batch of IPs stored in a text file using the `batch_lookup` function. This can be configured to output the results in various formats (CSV, JSON, GeoJSON).

## Configuration

### API Token
The tool uses the IPinfo API for geolocation data. You need to provide an API token. 

- Inside `config.py`, set your API token:

```python
API_TOKEN = 'your_api_token_here'
```

## File Structure

```
/src
  ├── __init__.py          # Intiate python
  ├── batch_lookup.py      # Batch processing script
  ├── file_export.py       # File export functions
  ├── ip_geolocation.py    # Geolocation API interaction
/config.py                 # Configuration file (API token)
/requirements.txt          # Python dependencies
/ip_geoloc.py              # CLI entry point for geolocation tool - Main Tool
```

## Contributing

Feel free to fork this repository and contribute improvements, bug fixes, or new features via pull requests.

## Acknowledgments

- [ipinfo.io](https://ipinfo.io/) for providing the IP geolocation API.
