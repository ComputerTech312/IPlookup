import argparse
import requests
import shodan
import os

def get_ip_info(ip):
    url = f'https://ipapi.co/{ip}/json/'
    response = requests.get(url)
    data = response.json()
    print('IP Information:')
    print('----------------')
    print(f'IP: {data["ip"]}')
    print(f'City: {data["city"]}')
    print(f'Region: {data["region"]}')
    print(f'Country: {data["country_name"]}')
    print(f'Postal Code: {data["postal"]}')
    print(f'Latitude: {data["latitude"]}')
    print(f'Longitude: {data["longitude"]}')
    print(f'ISP: {data["org"]}')
    
def lookup_dns(api,dns):
    try:
        # Perform the search
        results = api.search(f"dns:{dns}")

        # Print the results
        print(f'Results found: {results["total"]}')
        for result in results['matches']:
            print(f'IP: {result["ip_str"]}')
            print(f'Port: {result["port"]}')
            print(f'Org: {result["org"]}')
            print(f'Domain: {result["domains"]}')
            print('-----------------')

    except shodan.APIError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A tool for looking up IP and DNS information')
    parser.add_argument('-i', '--ip', help='Lookup IP information')
    parser.add_argument('-s', '--shodan', help='Lookup DNS information with shodan api')
    args = parser.parse_args()
    API_KEY = 'oWeBVwATG5lERwEGUrROOKNdvjIhrzdR'

    if args.ip:
        ip = args.ip.strip()
        get_ip_info(ip)
    elif args.shodan:
        if API_KEY is None:
            print("Error: SHODAN_API_KEY environment variable not set")
        dns = args.shodan
        api = shodan.Shodan(API_KEY)
        lookup_dns(api, dns)
    else:
        parser.print_help()
