#!/usr/bin/python3
import shodan
import argparse
import json
import requests

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Search Shodan')
parser.add_argument('-i', '--ip', help='Search by IP address')
parser.add_argument('-d', '--dns', help='Search by DNS name')
parser.add_argument('-p', '--port', help='Search by port number')
args = parser.parse_args()

# Instantiate the API clients
api_key = "Your-API-Key"
shodan_api = shodan.Shodan(api_key)

# Perform the search
if args.ip:
    shodan_results = shodan_api.host(args.ip)
    ip_api_url = f'http://ip-api.com/json/{args.ip}'
    ip_api_results = requests.get(ip_api_url).json()

    print(f'Results for IP address {args.ip}:')
    print(f'Location: {ip_api_results["city"]}, {ip_api_results["country"]}')
    print(f'Latitude: {ip_api_results["lat"]}')
    print(f'Longitude: {ip_api_results["lon"]}')
    print(f'ISP: {ip_api_results["isp"]}')
    #print(json.dumps(shodan_results, indent=2))
elif args.dns:
    shodan_results = shodan_api.search(args.dns)
    print(f'Results for DNS name {args.dns}:')
    ips_set = set()
    for result in shodan_results['matches']:
        if result['ip_str'] not in ips_set:
            print("City: ", result['location']['city'])
            print("Country: ", result['location']['country_name'])
            print("IP: ", result['ip_str'])
            print("ISP: ", result['isp'])
            print("Latitude: ", result['location']['latitude'])
            print("Longitude: ", result['location']['longitude'])
            print("------------------------------")
            ips_set.add(result['ip_str'])
elif args.port:
    shodan_host = shodan_api.host(args.port)
    print(f'Open ports for host {args.port}:')
    for item in shodan_host['data']:
        print(item['port'])
else:
    print('You must provide an IP address, DNS name, or port number to search for.')
