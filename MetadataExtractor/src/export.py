import csv
import json

def export_to_csv(metadata, output_file):
    """Export extracted metadata to a CSV file."""
    if not metadata:
        print("No data to export.")
        return

    with open(f"{output_file}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = metadata[0].keys()  # Get the fieldnames from the first dictionary
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in metadata:
            writer.writerow(data)

    print(f"Metadata exported to {output_file}.csv")

def export_to_json(metadata, output_file):
    """Export extracted metadata to a JSON file."""
    if not metadata:
        print("No data to export.")
        return

    with open(f"{output_file}.json", 'w', encoding='utf-8') as jsonfile:
        json.dump(metadata, jsonfile, indent=4)

    print(f"Metadata exported to {output_file}.json")
