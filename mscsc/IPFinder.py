import requests
import os
from dotenv import load_dotenv
import json
from tabulate import tabulate

load_dotenv()
url = "https://api.ipgeolocation.io/ipgeo"


def main():
    ip = get_ip()
    data = get_data(ip)
    fetch_data(data)


def get_ip():
   return input("Enter the IP address: ")

def get_data(ip):
    try:
        res = requests.get(f"{url}?apiKey={os.getenv("IP_API_KEY")}&ip={ip}")
        return res.json()
    except Exception as e:
        print(e)

def fetch_data(data):
    print_options(data)
    data_structure = [data]
    while True:
        try:
            choice = input("Input Options:\n1) Enter field name\n2) Enter 'all' to print all data\n3) Enter 'prev' to print previous data\n4) type 't' to print table\nEnter your choice: ").strip().lower()
        except KeyboardInterrupt:
            break

        if choice == "all":
            print(json.dumps(data, indent=4))
            print("\n" + "-" * 50 + "\n")
            continue

        if choice == "t":
            print_options(data)
            print("\n" + "-" * 50 + "\n")
            continue

        if choice == "prev":
            if len(data_structure) == 1:
                print("\nNo previous data")
                data_structure.pop()
            else :
                data_structure.pop()
                print_options(data_structure[-1])

            print("\n" + "-" * 50 + "\n")
            continue

        if choice in data_structure[-1] and choice != "":
            data_structure.append(data_structure[-1][choice])
            print(f"\n{choice.capitalize()} : {data_structure[-1]}")
            print("\n" + "-" * 50 + "\n")
        else:
            print("\nInvalid field")
            print("\n" + "-" * 50 + "\n")


def print_options(data):
    headers = ["Key", "Value"]
    rows = [
        ["IP", data["ip"]],
        ["Continent", data["continent_name"]],
        ["Country", data["country_name"]],
        ["District", data["district"]],
        ["City", data["city"]],
        ["ISP", data["isp"]],
        ["Organization", data["organization"]],
        ["Time", data["time_zone"]["current_time"]],
    ]

    print(tabulate(rows, headers=headers, tablefmt="rounded_grid"))


if __name__ == "__main__":
    main()