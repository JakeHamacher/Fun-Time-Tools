import csv
import json
from src.ip_geolocation import get_ip_info

def batch_lookup(input_data, output_file, output_format='csv'):
    # If input_data is a file path, read IPs from the file
    if isinstance(input_data, str):
        with open(input_data, 'r') as file:
            ips = file.readlines()
    else:
        # If input_data is already a list of IPs, use it directly
        ips = input_data
    
    # Remove any extra spaces or newlines
    ips = [ip.strip() for ip in ips]

    # Debugging: Check if we are getting IPs properly
    print(f"IPs to lookup: {ips}")  # Debug line

    # Fetch the geolocation data
    results = []
    for ip in ips:
        result = get_ip_info(ip)
        print(f"Result for {ip}: {result}")  # Debug line
        if result:
            results.append(result)

    # If no results were obtained, print a message
    if not results:
        print("No geolocation data found for the provided IPs.")
        return []

    # Write the output to a file
    fieldnames = ['ip', 'city', 'region', 'country', 'location', 'org', 'asn']
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

    return results  # Return results after processing
