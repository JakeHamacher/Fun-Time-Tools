# src/file_export.py

import csv

def export_to_csv(data: list, filename: str):
    """
    Exports the lookup data to a CSV file.
    :param data: The list of dictionaries to write to the CSV.
    :param filename: The name of the output file.
    """
    if data:
        keys = data[0].keys()
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"Data exported to {filename}")
    else:
        print("No data to export.")
