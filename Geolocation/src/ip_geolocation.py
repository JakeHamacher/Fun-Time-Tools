# src/ip_geolocation.py

import requests
from config import API_TOKEN

def get_ip_info(ip: str):
    """
    Fetches IP geolocation and ASN info using an external API.
    :param ip: The IP address to look up.
    :return: A dictionary containing the geolocation and ASN data.
    """
    url = f"https://ipinfo.io/{ip}/json?token={API_TOKEN}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        data = response.json()

        # Check if the response contains the expected data
        if 'ip' not in data:
            raise ValueError("Invalid response: 'ip' key not found")

        # Extract necessary information
        ip_data = {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "location": data.get("loc"),
            "org": data.get("org"),
            "asn": data.get("org").split(" ")[0] if data.get("org") else None  # Simple method to extract ASN
        }
        return ip_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {ip}: {e}")
    except ValueError as e:
        print(f"Error processing data for {ip}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {ip}: {e}")
    return None
