import shodan
import argparse
import json

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Search Shodan')
parser.add_argument('-i', '--ip', help='Search by IP address')
parser.add_argument('-d', '--dns', help='Search by DNS name')
parser.add_argument('-p', '--port', help='Search by port number')
args = parser.parse_args()

# Instantiate the API client with your own API key
api_key = "oWeBVwATG5lERwEGUrROOKNdvjIhrzdR"
api = shodan.Shodan(api_key)

import json

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Search Shodan')
parser.add_argument('-i', '--ip', help='Search by IP address')
parser.add_argument('-d', '--dns', help='Search by DNS name')
parser.add_argument('-p', '--port', help='Search by port number')
args = parser.parse_args()

# Instantiate the API client with your own API key
api_key = "Your-API-Key"
api = shodan.Shodan(api_key)

# Perform the search
if args.ip:
    results = api.host(args.ip)
    print(f'Results for IP address {args.ip}:')
    print(json.dumps(results, indent=2))
elif args.dns:
    results = api.search(args.dns)
    print(f'Results for DNS name {args.dns}:')
    ips_set = set()
    for result in results['matches']:
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
    host = api.host(args.port)
    print(f'Open ports for host {args.port}:')
    for item in host['data']:
        print(item['port'])
else:
    print('You must provide an IP address, DNS name, or port number to search for.')

