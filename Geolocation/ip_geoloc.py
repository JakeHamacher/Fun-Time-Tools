import argparse
from src.batch_lookup import batch_lookup
from src.file_export import export_to_csv

def read_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    parser = argparse.ArgumentParser(description='IP Geolocation Tool')
    parser.add_argument('ips', nargs='*', help='List of IP addresses to lookup')
    parser.add_argument('--input-file', help='File containing IP addresses to lookup')
    parser.add_argument('--output', help='Output CSV file', default='output.csv')
    args = parser.parse_args()

    if args.input_file:
        # If input file is provided, read the IPs from the file
        ips = read_ips_from_file(args.input_file)
    else:
        # If no input file, use IPs from the command line argument
        ips = args.ips

    # Pass the list of IPs or file path to batch_lookup
    results = batch_lookup(ips if isinstance(ips, list) else args.input_file, args.output)
    export_to_csv(results, args.output)

if __name__ == '__main__':
    main()
