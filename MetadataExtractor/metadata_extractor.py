import argparse
import os
import json
from src.extract_metadata import extract_metadata
from src.export import export_to_csv, export_to_json

def main():
    parser = argparse.ArgumentParser(description='Metadata Extractor Tool')
    parser.add_argument('files', nargs='*', help='Files to extract metadata from')
    parser.add_argument('--input-dir', help='Directory containing files to extract metadata from')
    parser.add_argument('--output', help='Output file for exported metadata (CSV or JSON)', default='output')
    parser.add_argument('--output-format', choices=['csv', 'json'], default='csv', help='Format of the output file')
    args = parser.parse_args()

    # Gather files
    files = []
    if args.files:
        files.extend(args.files)
    if args.input_dir:
        for filename in os.listdir(args.input_dir):
            filepath = os.path.join(args.input_dir, filename)
            if os.path.isfile(filepath):
                files.append(filepath)

    # Extract metadata from each file
    metadata = []
    for file in files:
        print(f"Extracting metadata from: {file}")
        file_metadata = extract_metadata(file)
        if file_metadata:
            metadata.append(file_metadata)
    
    if not metadata:
        print("No metadata found.")
        return

    # Export results to the specified format
    if args.output_format == 'csv':
        export_to_csv(metadata, args.output)
    elif args.output_format == 'json':
        export_to_json(metadata, args.output)

    print(f"Metadata extraction complete. Results saved to {args.output}.{args.output_format}")

if __name__ == '__main__':
    main()
